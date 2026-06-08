"""
Pizza Production Optimization Engine - Example Usage
=====================================================

This script demonstrates how to use the pizza production optimizer
to calculate the maximum profit production plan.
"""

from solver import solve_multivariable

def example_basic():
    """Basic example with 2 pizza types and 4 ingredients"""
    print("=" * 70)
    print("EXAMPLE 1: Basic 2-Pizza Optimization")
    print("=" * 70)
    
    # Available inventory
    stocks = {
        "Flour": 150.0,        # kg
        "Cheese": 50.0,        # kg
        "Sauce": 160.0,        # kg
    }
    
    # Pizza recipes (ingredients per unit)
    recipes = {
        "Mozzarella": {
            "Flour": 0.5,
            "Cheese": 0.3,
            "Sauce": 0.2,
        },
        "Pepperoni": {
            "Flour": 0.5,
            "Cheese": 0.2,
            "Sauce": 0.2,
        }
    }
    
    # Profit per pizza (in dollars)
    profits = {
        "Mozzarella": 12.0,
        "Pepperoni": 15.0
    }
    
    print("\n📦 INVENTORY:")
    for ingredient, stock in stocks.items():
        print(f"  {ingredient:15} {stock:8.1f} units")
    
    print("\n🍕 RECIPES (per pizza):")
    for pizza, recipe in recipes.items():
        print(f"\n  {pizza}:")
        for ingredient, amount in recipe.items():
            print(f"    - {ingredient:15} {amount:6.2f} units")
    
    print("\n💰 PROFIT PER PIZZA:")
    for pizza, profit in profits.items():
        print(f"  {pizza:15} ${profit:7.2f}")
    
    # Run optimization
    result = solve_multivariable(stocks, recipes, profits)
    
    if result["success"]:
        print("\n" + "=" * 70)
        print("✅ OPTIMAL PRODUCTION PLAN")
        print("=" * 70)
        
        print("\n🎯 PRODUCTION QUANTITIES:")
        for pizza, qty in result["production_plan"].items():
            print(f"  {pizza:20} {qty:8.0f} pizzas")
        
        print(f"\n💵 TOTAL PROFIT: ${result['total_profit']:,.2f}")
        
        print("\n📊 PROFIT BREAKDOWN:")
        for pizza, profit in result["profit_breakdown"].items():
            print(f"  {pizza:20} ${profit:10,.2f}")
        
        print("\n📈 INGREDIENT USAGE:")
        for ingredient, usage in result["ingredient_usage"].items():
            status = "⚠️  BOTTLENECK" if usage["bottleneck"] else "✓"
            print(f"  {ingredient:15} {usage['used']:8.2f} / {usage['stock']:8.2f} ({usage['percent']:5.1f}%) {status}")
        
        if result["bottleneck_ingredients"]:
            print(f"\n⛔ BOTTLENECK INGREDIENTS: {', '.join(result['bottleneck_ingredients'])}")
            print("    These ingredients limit your maximum production.")
    else:
        print(f"\n❌ Optimization failed: {result['message']}")
    
    return result


def example_advanced():
    """Advanced example with 4 pizza types and 6 ingredients"""
    print("\n\n" + "=" * 70)
    print("EXAMPLE 2: Advanced 4-Pizza Optimization")
    print("=" * 70)
    
    # Larger inventory for premium pizzeria
    stocks = {
        "Flour": 500.0,
        "Cheese": 200.0,
        "Sauce": 400.0,
        "Pepperoni": 80.0,
        "Vegetables": 150.0,
    }
    
    # Four different pizza types
    recipes = {
        "Classic Mozzarella": {
            "Flour": 0.5,
            "Cheese": 0.4,
            "Sauce": 0.2,
            "Pepperoni": 0.0,
            "Vegetables": 0.0,
        },
        "Pepperoni Deluxe": {
            "Flour": 0.5,
            "Cheese": 0.3,
            "Sauce": 0.2,
            "Pepperoni": 0.15,
            "Vegetables": 0.0,
        },
        "Veggie Supreme": {
            "Flour": 0.5,
            "Cheese": 0.25,
            "Sauce": 0.25,
            "Pepperoni": 0.0,
            "Vegetables": 0.3,
        },
        "Meat Lovers": {
            "Flour": 0.5,
            "Cheese": 0.3,
            "Sauce": 0.2,
            "Pepperoni": 0.2,
            "Vegetables": 0.05,
        }
    }
    
    # Different profit margins
    profits = {
        "Classic Mozzarella": 10.0,
        "Pepperoni Deluxe": 14.0,
        "Veggie Supreme": 13.0,
        "Meat Lovers": 16.0,
    }
    
    print("\n📦 INVENTORY:")
    for ingredient, stock in stocks.items():
        print(f"  {ingredient:20} {stock:8.1f} units")
    
    print("\n🍕 RECIPES (per pizza):")
    for pizza in sorted(recipes.keys()):
        print(f"\n  {pizza}:")
        for ingredient, amount in recipes[pizza].items():
            if amount > 0:
                print(f"    - {ingredient:20} {amount:6.2f} units")
    
    print("\n💰 PROFIT PER PIZZA:")
    for pizza, profit in sorted(profits.items()):
        print(f"  {pizza:25} ${profit:7.2f}")
    
    # Run optimization
    result = solve_multivariable(stocks, recipes, profits)
    
    if result["success"]:
        print("\n" + "=" * 70)
        print("✅ OPTIMAL PRODUCTION PLAN")
        print("=" * 70)
        
        print("\n🎯 PRODUCTION QUANTITIES:")
        total_pizzas = 0
        for pizza in sorted(result["production_plan"].keys()):
            qty = result["production_plan"][pizza]
            total_pizzas += qty
            print(f"  {pizza:25} {qty:8.0f} pizzas")
        
        print(f"\n  TOTAL PIZZAS: {total_pizzas:.0f}")
        print(f"\n💵 TOTAL PROFIT: ${result['total_profit']:,.2f}")
        
        print("\n📊 PROFIT BREAKDOWN:")
        for pizza in sorted(result["profit_breakdown"].keys()):
            profit = result["profit_breakdown"][pizza]
            print(f"  {pizza:25} ${profit:10,.2f}")
        
        print("\n📈 INGREDIENT USAGE:")
        for ingredient in sorted(result["ingredient_usage"].keys()):
            usage = result["ingredient_usage"][ingredient]
            status = "⚠️  BOTTLENECK" if usage["bottleneck"] else "✓"
            print(f"  {ingredient:20} {usage['used']:8.2f} / {usage['stock']:8.2f} ({usage['percent']:5.1f}%) {status}")
        
        if result["bottleneck_ingredients"]:
            print(f"\n⛔ BOTTLENECK INGREDIENTS:")
            for ingredient in result["bottleneck_ingredients"]:
                print(f"  - {ingredient}")
            print("\n💡 TIP: Consider increasing inventory for bottleneck ingredients")
            print("        to unlock higher total production.")
    else:
        print(f"\n❌ Optimization failed: {result['message']}")
    
    return result


if __name__ == "__main__":
    print("\n" + "🍕" * 35)
    print("PIZZA PRODUCTION OPTIMIZATION ENGINE")
    print("🍕" * 35 + "\n")
    
    # Run examples
    result1 = example_basic()
    result2 = example_advanced()
    
    print("\n\n" + "=" * 70)
    print("✅ All examples completed successfully!")
    print("=" * 70)
    print("\nNext Steps:")
    print("1. Adjust the stocks, recipes, and profits in these examples")
    print("2. Run the script again to see how the optimal plan changes")
    print("3. Use the /api/solve endpoint with mode='optimize' in your web app")
    print("\nAPI Usage:")
    print("""
    POST /api/solve
    {
        "mode": "optimize",
        "stocks": {"Flour": 150, "Cheese": 50, ...},
        "recipes": {
            "pizza1": {"Flour": 0.5, "Cheese": 0.3, ...},
            "pizza2": {...}
        },
        "profits": {"pizza1": 12.0, "pizza2": 15.0, ...}
    }
    """)
