"""
Test suite for Pizza Production Optimization Engine
"""

import sys
from solver import solve_multivariable


def test_basic_two_pizza():
    """Test basic 2-pizza optimization"""
    print("\n" + "=" * 70)
    print("TEST 1: Basic 2-Pizza Optimization")
    print("=" * 70)
    
    stocks = {
        "flour": 150.0,
        "cheese": 50.0,
        "sauce": 160.0,
    }
    
    recipes = {
        "mozzarella": {
            "flour": 0.5,
            "cheese": 0.3,
            "sauce": 0.2,
        },
        "pepperoni": {
            "flour": 0.5,
            "cheese": 0.2,
            "sauce": 0.2,
        }
    }
    
    profits = {
        "mozzarella": 20.0,
        "pepperoni": 25.0
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    assert result["total_profit"] > 0, "Total profit should be positive"
    assert "mozzarella" in result["production_plan"], "Missing mozzarella in plan"
    assert "pepperoni" in result["production_plan"], "Missing pepperoni in plan"
    
    # Check bottleneck
    assert len(result["bottleneck_ingredients"]) > 0, "Should have at least one bottleneck"
    
    print("✅ PASSED")
    print(f"   Total Profit: ${result['total_profit']}")
    print(f"   Plan: {result['production_plan']}")
    print(f"   Bottleneck: {result['bottleneck_ingredients']}")
    
    return result


def test_four_pizza_advanced():
    """Test advanced 4-pizza optimization"""
    print("\n" + "=" * 70)
    print("TEST 2: Advanced 4-Pizza Optimization")
    print("=" * 70)
    
    stocks = {
        "flour": 500.0,
        "cheese": 200.0,
        "sauce": 400.0,
        "pepperoni": 80.0,
        "vegetables": 150.0,
    }
    
    recipes = {
        "classic": {
            "flour": 0.5,
            "cheese": 0.4,
            "sauce": 0.2,
            "pepperoni": 0.0,
            "vegetables": 0.0,
        },
        "pepperoni_deluxe": {
            "flour": 0.5,
            "cheese": 0.3,
            "sauce": 0.2,
            "pepperoni": 0.15,
            "vegetables": 0.0,
        },
        "veggie_supreme": {
            "flour": 0.5,
            "cheese": 0.25,
            "sauce": 0.25,
            "pepperoni": 0.0,
            "vegetables": 0.3,
        },
        "meat_lovers": {
            "flour": 0.5,
            "cheese": 0.3,
            "sauce": 0.2,
            "pepperoni": 0.2,
            "vegetables": 0.05,
        }
    }
    
    profits = {
        "classic": 10.0,
        "pepperoni_deluxe": 14.0,
        "veggie_supreme": 13.0,
        "meat_lovers": 16.0,
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    assert result["total_profit"] > 0, "Total profit should be positive"
    assert len(result["production_plan"]) == 4, "Should have 4 pizzas in plan"
    
    total_pizzas = sum(result["production_plan"].values())
    assert total_pizzas > 0, "Should produce at least one pizza"
    
    print("✅ PASSED")
    print(f"   Total Profit: ${result['total_profit']:.2f}")
    print(f"   Total Pizzas: {total_pizzas:.0f}")
    print(f"   Plan: {result['production_plan']}")
    print(f"   Bottlenecks: {result['bottleneck_ingredients']}")
    
    return result


def test_single_ingredient_constraint():
    """Test single ingredient constraint"""
    print("\n" + "=" * 70)
    print("TEST 3: Single Ingredient Constraint")
    print("=" * 70)
    
    stocks = {
        "flour": 100.0,
    }
    
    recipes = {
        "simple": {
            "flour": 1.0,
        }
    }
    
    profits = {
        "simple": 5.0,
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    assert result["production_plan"]["simple"] == 100.0, "Should produce exactly 100 pizzas"
    assert result["total_profit"] == 500.0, "Profit should be exactly 500"
    
    print("✅ PASSED")
    print(f"   Produced: {result['production_plan']['simple']:.0f} pizzas")
    print(f"   Total Profit: ${result['total_profit']}")
    
    return result


def test_profit_maximization():
    """Test that higher profit pizzas are prioritized"""
    print("\n" + "=" * 70)
    print("TEST 4: Profit Maximization Priority")
    print("=" * 70)
    
    stocks = {
        "flour": 100.0,
    }
    
    recipes = {
        "cheap_pizza": {
            "flour": 1.0,
        },
        "expensive_pizza": {
            "flour": 1.0,
        }
    }
    
    profits = {
        "cheap_pizza": 5.0,
        "expensive_pizza": 15.0,
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    
    # Should produce more expensive pizza or only expensive pizza
    if result["production_plan"]["cheap_pizza"] > 0 and result["production_plan"]["expensive_pizza"] > 0:
        # Both produced - check that expensive is >= cheap
        assert result["production_plan"]["expensive_pizza"] >= result["production_plan"]["cheap_pizza"], \
            "Should produce at least as many expensive pizzas"
    
    # Total profit should be maximized (favor expensive)
    expensive_only_profit = 100.0 * 15.0
    assert result["total_profit"] >= expensive_only_profit * 0.99, \
        "Should achieve near-maximum profit"
    
    print("✅ PASSED")
    print(f"   Plan: {result['production_plan']}")
    print(f"   Total Profit: ${result['total_profit']}")
    print(f"   Expensive Pizza contribution: ${result['profit_breakdown']['expensive_pizza']:.2f}")
    
    return result


def test_ingredient_usage_calculation():
    """Test that ingredient usage is calculated correctly"""
    print("\n" + "=" * 70)
    print("TEST 5: Ingredient Usage Calculation")
    print("=" * 70)
    
    stocks = {
        "flour": 50.0,
        "cheese": 30.0,
    }
    
    recipes = {
        "pizza": {
            "flour": 1.0,
            "cheese": 0.5,
        }
    }
    
    profits = {
        "pizza": 10.0,
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    
    qty = result["production_plan"]["pizza"]
    
    # Check flour usage
    flour_used = result["ingredient_usage"]["flour"]["used"]
    assert abs(flour_used - qty * 1.0) < 0.01, f"Flour usage incorrect: {flour_used} vs {qty}"
    
    # Check cheese usage
    cheese_used = result["ingredient_usage"]["cheese"]["used"]
    assert abs(cheese_used - qty * 0.5) < 0.01, f"Cheese usage incorrect: {cheese_used} vs {qty * 0.5}"
    
    print("✅ PASSED")
    print(f"   Produced: {qty:.2f} pizzas")
    print(f"   Flour: {flour_used:.2f} / {stocks['flour']:.2f}")
    print(f"   Cheese: {cheese_used:.2f} / {stocks['cheese']:.2f}")
    
    return result


def test_bottleneck_detection():
    """Test bottleneck ingredient detection"""
    print("\n" + "=" * 70)
    print("TEST 6: Bottleneck Detection")
    print("=" * 70)
    
    stocks = {
        "flour": 100.0,
        "cheese": 10.0,  # Limited
    }
    
    recipes = {
        "pizza": {
            "flour": 0.5,
            "cheese": 0.5,  # High cheese requirement
        }
    }
    
    profits = {
        "pizza": 10.0,
    }
    
    result = solve_multivariable(stocks, recipes, profits)
    
    assert result["success"], f"Test failed: {result.get('message')}"
    assert "cheese" in result["bottleneck_ingredients"], "Cheese should be bottleneck"
    
    cheese_usage = result["ingredient_usage"]["cheese"]
    assert cheese_usage["bottleneck"] == True, "Cheese should be marked as bottleneck"
    assert cheese_usage["percent"] >= 99.0, "Cheese should be 99%+ utilized"
    
    print("✅ PASSED")
    print(f"   Bottleneck: {result['bottleneck_ingredients']}")
    print(f"   Cheese usage: {cheese_usage['percent']:.1f}%")
    
    return result


def run_all_tests():
    """Run all tests"""
    print("\n" + "🍕" * 35)
    print("PIZZA PRODUCTION OPTIMIZATION - TEST SUITE")
    print("🍕" * 35)
    
    tests = [
        test_basic_two_pizza,
        test_four_pizza_advanced,
        test_single_ingredient_constraint,
        test_profit_maximization,
        test_ingredient_usage_calculation,
        test_bottleneck_detection,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    
    if failed == 0:
        print("✅ ALL TESTS PASSED!")
        return 0
    else:
        print(f"❌ {failed} TEST(S) FAILED")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
