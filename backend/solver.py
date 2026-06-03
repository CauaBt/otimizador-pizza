import math
from scipy.optimize import linprog
import numpy as np

def check_feasibility(x1, x2, recipes, stocks, tolerance=1e-6):
    """
    Checks if a point (x1, x2) satisfies all non-negativity and ingredient stock constraints.
    """
    if x1 < -tolerance or x2 < -tolerance:
        return False
    
    for ing, stock in stocks.items():
        used = recipes['pizza1'].get(ing, 0) * x1 + recipes['pizza2'].get(ing, 0) * x2
        if used > stock + tolerance:
            return False
            
    return True

def get_line_intersection(line1, line2):
    """
    Solves the linear system:
    A1*x1 + B1*x2 = C1
    A2*x1 + B2*x2 = C2
    Returns (x1, x2) or None if lines are parallel.
    """
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    
    det = A1 * B2 - A2 * B1
    if abs(det) < 1e-9:
        return None
        
    x1 = (C1 * B2 - C2 * B1) / det
    x2 = (A1 * C2 - A2 * C1) / det
    return (x1, x2)


def floor_quantity(value):
    """Returns a non-negative integer quantity by flooring any fractional value."""
    return int(math.floor(max(0.0, float(value))))


def calculate_usage(x1, x2, recipes, stocks):
    """
    Calculates ingredient usage details (amount used and percentage used) for a production quantity.
    """
    usage = {}
    for ing, stock in stocks.items():
        used = recipes['pizza1'].get(ing, 0) * x1 + recipes['pizza2'].get(ing, 0) * x2
        # Clamp to avoid floating point issues
        used = max(0.0, min(used, stock))
        percent = (used / stock * 100) if stock > 0 else 0
        usage[ing] = {
            "used": round(used, 2),
            "stock": stock,
            "percent": round(percent, 1),
            "bottleneck": percent >= 99.9
        }
    return usage

def solve_1d(stocks, recipe, profit, pizza_var='x1'):
    """
    Solves the 1-variable LP optimization case.
    Returns optimal quantity, total profit, and ingredient usages.
    """
    max_q = float('inf')
    bottleneck_ing = None
    
    # Calculate limits imposed by each ingredient recipe
    for ing, stock in stocks.items():
        req = recipe.get(ing, 0)
        if req > 0:
            limit = stock / req
            if limit < max_q:
                max_q = limit
                bottleneck_ing = ing
                
    if max_q == float('inf'):
        max_q = 0.0
        
    optimal_q = floor_quantity(max_q)
    total_profit = round(optimal_q * profit, 2)
    
    # Pack recipe into format expected by calculate_usage
    if pizza_var == 'x1':
        fake_recipes = {
            'pizza1': recipe,
            'pizza2': {k: 0.0 for k in recipe}
        }
        x1_val = optimal_q
        x2_val = 0.0
        vertices = [[0.0, 0.0], [optimal_q, 0.0]]
    else:
        fake_recipes = {
            'pizza1': {k: 0.0 for k in recipe},
            'pizza2': recipe
        }
        x1_val = 0.0
        x2_val = optimal_q
        vertices = [[0.0, 0.0], [0.0, optimal_q]]
    
    usage = calculate_usage(x1_val, x2_val, fake_recipes, stocks)
    
    return {
        "success": True,
        "optimal_x1": x1_val,
        "optimal_x2": x2_val,
        "total_profit": total_profit,
        "usage": usage,
        "vertices": vertices
    }

def solve_2d(stocks, recipes, profits):
    """
    Solves the 2-variable LP optimization case (Modo Mix).
    Uses Vertex Enumeration to find the optimal mix of Pizza 1 and Pizza 2.
    """
    # Define constraint lines: A*x1 + B*x2 = C
    # Axis boundaries
    lines = [
        (1.0, 0.0, 0.0), # x1 = 0
        (0.0, 1.0, 0.0)  # x2 = 0
    ]
    
    # Ingredient constraints
    for ing, stock in stocks.items():
        a1 = recipes['pizza1'].get(ing, 0.0)
        a2 = recipes['pizza2'].get(ing, 0.0)
        if a1 > 0.0 or a2 > 0.0:
            lines.append((a1, a2, stock))
            
    # Find all intersection points
    raw_points = []
    num_lines = len(lines)
    for i in range(num_lines):
        for j in range(i + 1, num_lines):
            pt = get_line_intersection(lines[i], lines[j])
            if pt is not None:
                # Clamp small negative floats to 0.0
                x1, x2 = pt
                if -1e-6 <= x1 < 0:
                    x1 = 0.0
                if -1e-6 <= x2 < 0:
                    x2 = 0.0
                raw_points.append((x1, x2))
                
    # Filter only feasible intersection points (vertices of the feasible region)
    feasible_vertices = []
    for pt in raw_points:
        if check_feasibility(pt[0], pt[1], recipes, stocks):
            # Check for duplicates
            is_dup = False
            for v in feasible_vertices:
                if math.hypot(pt[0] - v[0], pt[1] - v[1]) < 1e-4:
                    is_dup = True
                    break
            if not is_dup:
                feasible_vertices.append(pt)
                
    if not feasible_vertices:
        return {
            "success": False,
            "message": "Região viável vazia."
        }
        
    # Sort vertices counter-clockwise around their centroid
    cx = sum(v[0] for v in feasible_vertices) / len(feasible_vertices)
    cy = sum(v[1] for v in feasible_vertices) / len(feasible_vertices)
    
    # Sort by polar angle relative to centroid
    feasible_vertices.sort(key=lambda v: math.atan2(v[1] - cy, v[0] - cx))
    
    # Find the vertex that maximizes total profit: Z = c1*x1 + c2*x2
    best_profit = -1.0
    best_vertex = (0.0, 0.0)
    
    c1 = profits.get('pizza1', 0.0)
    c2 = profits.get('pizza2', 0.0)
    
    for v in feasible_vertices:
        profit = c1 * v[0] + c2 * v[1]
        if profit > best_profit:
            best_profit = profit
            best_vertex = v
            
    optimal_x1 = floor_quantity(best_vertex[0])
    optimal_x2 = floor_quantity(best_vertex[1])
    total_profit = round(c1 * optimal_x1 + c2 * optimal_x2, 2)
    
    usage = calculate_usage(optimal_x1, optimal_x2, recipes, stocks)
    
    # Format vertices for frontend JSON response
    formatted_vertices = [[round(v[0], 2), round(v[1], 2)] for v in feasible_vertices]
    
    # Also extract raw constraint boundary lines for charting
    # Each line can be drawn by its intercepts with graph bounds
    chart_lines = []
    for ing, stock in stocks.items():
        a1 = recipes['pizza1'].get(ing, 0.0)
        a2 = recipes['pizza2'].get(ing, 0.0)
        if a1 > 0 or a2 > 0:
            chart_lines.append({
                "ingredient": ing,
                "a1": a1,
                "a2": a2,
                "stock": stock
            })
            
    return {
        "success": True,
        "optimal_x1": optimal_x1,
        "optimal_x2": optimal_x2,
        "total_profit": total_profit,
        "usage": usage,
        "vertices": formatted_vertices,
        "constraint_lines": chart_lines
    }


def solve_multivariable(stocks, recipes, profits):
    """
    Solves the N-variable LP optimization case using scipy.optimize.linprog.
    Supports any number of pizza types and ingredients.
    
    Parameters:
    - stocks: dict of ingredient -> available quantity
    - recipes: dict of pizza_name -> dict of ingredient -> quantity needed
    - profits: dict of pizza_name -> profit per unit
    
    Returns: JSON-serializable dict with optimal production plan and profit analysis
    """
    try:
        # Extract pizza names in consistent order
        pizza_names = sorted(recipes.keys())
        n_pizzas = len(pizza_names)
        
        if n_pizzas == 0:
            return {
                "success": False,
                "message": "No pizza recipes provided."
            }
        
        # Extract ingredient names in consistent order from both stocks and recipes
        ingredient_names = sorted(
            set(stocks.keys()) |
            {ingredient for recipe in recipes.values() for ingredient in recipe.keys()}
        )
        n_ingredients = len(ingredient_names)
        
        if n_ingredients == 0:
            return {
                "success": False,
                "message": "No ingredient stocks or recipe ingredients provided."
            }
        
        # Build profit vector (negative for linprog since it minimizes)
        c = np.array([
            -profits.get(pizza, 0.0) for pizza in pizza_names
        ], dtype=float)
        
        # Build constraint matrix A_ub and bounds b_ub
        # Constraint: sum(a_ij * x_j) <= b_i for each ingredient i
        A_ub = []
        b_ub = []
        
        for ingredient in ingredient_names:
            stock = stocks.get(ingredient, 0.0)
            constraint_row = [
                recipes[pizza].get(ingredient, 0.0)
                for pizza in pizza_names
            ]
            A_ub.append(constraint_row)
            b_ub.append(float(stock))
        
        A_ub = np.array(A_ub, dtype=float)
        b_ub = np.array(b_ub, dtype=float)
        
        # Bounds: all quantities >= 0
        x_bounds = [(0, None) for _ in range(n_pizzas)]
        
        # Solve LP
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')
        
        if not result.success:
            return {
                "success": False,
                "message": f"Optimization failed: {result.message}"
            }
        
        # Extract solution
        optimal_quantities = result.x
        floored_quantities = [floor_quantity(q) for q in optimal_quantities]
        total_profit = sum(
            floored_quantities[i] * profits.get(pizza_names[i], 0.0)
            for i in range(n_pizzas)
        )
        
        # Build production plan
        production_plan = {}
        for i, pizza in enumerate(pizza_names):
            production_plan[pizza] = floored_quantities[i]
        
        # Calculate ingredient usage and remaining inventory
        ingredient_usage = {}
        remaining_inventory = {}
        for i, ingredient in enumerate(ingredient_names):
            stock = stocks.get(ingredient, 0.0)
            used = sum(
                floored_quantities[j] * recipes[pizza_names[j]].get(ingredient, 0.0)
                for j in range(n_pizzas)
            )
            used = float(used)
            remaining = max(0.0, stock - used)
            percent = (used / stock * 100) if stock > 0 else 0
            
            ingredient_usage[ingredient] = {
                "used": round(used, 2),
                "stock": stock,
                "percent": round(percent, 1),
                "remaining": round(remaining, 2),
                "bottleneck": percent >= 99.0
            }
            remaining_inventory[ingredient] = round(remaining, 2)
        
        # Identify bottleneck ingredients
        bottlenecks = [ing for ing, data in ingredient_usage.items() if data["bottleneck"]]
        
        return {
            "success": True,
            "production_plan": production_plan,
            "total_profit": round(total_profit, 2),
            "ingredient_usage": ingredient_usage,
            "remaining_inventory": remaining_inventory,
            "bottleneck_ingredients": bottlenecks,
            "profit_breakdown": {
                pizza: round(floored_quantities[i] * profits.get(pizza, 0.0), 2)
                for i, pizza in enumerate(pizza_names)
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "message": f"Error during optimization: {str(e)}"
        }
