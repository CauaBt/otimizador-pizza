# 🍕 Pizza Production Optimizer - Quick Start Guide

## What It Does

Automatically calculates **the exact number of each pizza to produce** to make the most money, given your current ingredient inventory.

## Input Requirements

1. **Your Inventory** (what you have)
   - Example: 150 kg flour, 50 kg cheese, 25 kg butter, 160 kg sauce

2. **Pizza Recipes** (what each pizza needs)
   - Example: Mozzarella pizza = 0.5 kg flour + 0.3 kg cheese + 0.2 kg sauce + 0.2 kg butter

3. **Profit Per Pizza** (how much you make per sale)
   - Example: Mozzarella = $12, Pepperoni = $15

## Output: Your Optimal Production Plan

The optimizer returns:
- ✅ **How many of each pizza to make**
- ✅ **Your total profit**
- ✅ **Which ingredients are your bottlenecks** (limiting your production)
- ✅ **How much of each ingredient you'll use**

---

## How to Use

### Method 1: Run Python Script Locally

```bash
cd backend
pip install -r requirements.txt
python optimize_example.py
```

**Output Example:**
```
🎯 PRODUCTION QUANTITIES:
  Mozzarella          125 pizzas
  Pepperoni             0 pizzas

💵 TOTAL PROFIT: $1,500.00

⛔ BOTTLENECK INGREDIENTS:
  - Butter
```

### Method 2: Use the Web API

Send a POST request to `http://localhost:5000/api/solve`:

```json
{
  "mode": "optimize",
  "stocks": {
    "flour": 150,
    "cheese": 50,
    "sauce": 160,
    "butter": 25
  },
  "recipes": {
    "mozzarella": {
      "flour": 0.5,
      "cheese": 0.3,
      "sauce": 0.2,
      "butter": 0.2
    },
    "pepperoni": {
      "flour": 0.5,
      "cheese": 0.2,
      "sauce": 0.2,
      "butter": 0.15
    }
  },
  "profits": {
    "mozzarella": 12.0,
    "pepperoni": 15.0
  }
}
```

**Response:**
```json
{
  "success": true,
  "production_plan": {
    "mozzarella": 125.0,
    "pepperoni": 0.0
  },
  "total_profit": 1500.00,
  "bottleneck_ingredients": ["butter"],
  ...
}
```

---

## Understanding the Results

### Production Plan
Tells you exactly what to make:
- **125 Mozzarella pizzas** → 125 × $12 = $1,500
- **0 Pepperoni pizzas** → 0 × $15 = $0
- **Total Profit: $1,500**

### Why This Plan?
- **Butter is the bottleneck** (you only have 25 kg)
- Both pizzas need 0.2 kg butter
- 25 kg ÷ 0.2 kg/pizza = 125 pizzas max
- Mozzarella is chosen because it's produced first in the sorting

### How to Make More Money?

**Option 1: Get more butter**
- If you had 40 kg butter → could make different mix
- Might make both pizzas if other ingredients allow

**Option 2: Adjust recipes**
- Use less butter per pizza
- Use cheaper ingredients

**Option 3: Change prices**
- Increase price of profitable pizzas
- Better margins = more profit with same production

---

## Real-World Scenario

### Scenario: Italian Pizzeria

**Your Inventory Today:**
```
Flour:     500 kg
Cheese:    200 kg
Sauce:     400 kg
Butter:    100 kg
Pepperoni:  80 kg
Vegetables: 150 kg
```

**Your 4 Pizzas:**
1. **Classic** ($10) - basic mozzarella
2. **Pepperoni Deluxe** ($14) - premium with pepperoni
3. **Veggie Supreme** ($13) - vegetarian
4. **Meat Lovers** ($16) - maximum profit

**Optimal Plan Might Be:**
```
Classic:          100 pizzas
Pepperoni Deluxe: 300 pizzas
Veggie Supreme:   150 pizzas
Meat Lovers:      200 pizzas
────────────────────────
TOTAL PROFIT:    $8,500
```

**Analysis:**
- Meat Lovers = highest price → make lots
- Pepperoni Deluxe = good profit → make many
- Veggie = lower profit → make only what ingredients allow
- Classic = lowest profit → make few

---

## Key Concepts

### Bottleneck Ingredient
- The ingredient limiting your production
- **At 100% utilization**
- Example: "You'd make 50% more pizzas if you had 50% more butter"

### Profit Breakdown
Shows contribution of each pizza:
- High numbers = that pizza type is worth making
- Zero = don't make that pizza

### Ingredient Efficiency
- **>99% used** = Efficient! (don't waste this)
- **<50% used** = Waste (consider reducing stock or changing recipes)

---

## Common Use Cases

### 1. Daily Production Planning
Run optimizer every morning with today's inventory and market prices

### 2. Purchasing Decisions
See which ingredient gives the best ROI:
- If butter is bottleneck → buy more butter
- If cheese sits unused → don't reorder

### 3. Menu Pricing
Identify which pizzas are most profitable:
- High profit → keep that price high
- Low profit → consider price increase or recipe change

### 4. Inventory Management
Plan what ingredients to order:
- Buy more of ingredients with low stock that create bottlenecks
- Reduce orders of ingredients with excess

### 5. Recipe Optimization
Test recipe changes:
- "What if we use 10% less butter?"
- "What if we add premium cheese?"
- Run optimizer to see impact on profit

---

## Tips for Best Results

### ✅ DO:
- Update inventory regularly
- Use realistic profit numbers
- Include all ingredients in recipes
- Test different scenarios

### ❌ DON'T:
- Use negative quantities
- Forget ingredient units (use consistent units)
- Leave recipes incomplete
- Ignore bottleneck ingredients

---

## Scaling Up

The optimizer can handle:
- **100+ pizzas** 
- **50+ ingredients**
- **Complex recipes** with many components

Just send the data and it will find the optimal plan in milliseconds.

---

## Need Help?

1. **Check OPTIMIZATION_API.md** for detailed API documentation
2. **Review optimize_example.py** for code examples
3. **Verify your data**:
   - All quantities > 0?
   - All recipes complete?
   - Reasonable profit values?

---

## Example: Try It Yourself

**Your inventory:**
- Flour: 100 kg
- Cheese: 40 kg
- Sauce: 80 kg

**Your pizzas:**
- Basic ($8): 0.5 flour, 0.2 cheese, 0.2 sauce
- Premium ($15): 0.5 flour, 0.4 cheese, 0.2 sauce

**Question:** How many of each should you make?

**Answer:** Run the optimizer!
- If Basic dominates (due to cheese costs), you'll make mostly Basic
- If Premium profit is high enough, you'll make the mix that uses all your cheese

The optimizer finds this instantly!

