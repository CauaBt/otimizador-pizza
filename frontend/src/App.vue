<template>
  <div class="dashboard-wrapper">
    <!-- Header -->
    <header class="main-header">
      <div class="logo-area">
        <Pizza class="logo-icon text-primary" />
        <div class="logo-text">
          <h1>Otimiza Pizza</h1>
          <p>Simulador de Produção de Pizzas</p>
        </div>
      </div>
      <div class="header-badge animate-fade-in">
        <span class="status-dot green pulse-glow"></span>
        <span>Simulador Ativo</span>
      </div>
    </header>

    <!-- Content Layout -->
    <main class="dashboard-grid">
      <!-- Sidebar Panel: Inputs -->
      <section class="control-panel glass-panel">
        <h2 class="panel-title">Painel de Configuração</h2>

        <!-- Available Stocks -->
        <div class="control-group">
          <h3 class="sub-group-title">Estoques de Ingredientes (Disponível)</h3>
          
          <!-- Flour (Farinha) -->
          <div class="slider-row">
            <div class="slider-header">
              <span class="ing-label"><Wheat class="ing-icon text-indigo" /> Farinha</span>
              <div class="input-unit-wrapper">
                <input type="number" v-model.number="stocks.farinha" min="0" max="500" class="num-input" />
                <span class="unit">kg</span>
              </div>
            </div>
            <input type="range" v-model.number="stocks.farinha" min="0" max="500" class="range-slider" />
          </div>

          <!-- Butter (Manteiga) -->
          <div class="slider-row">
            <div class="slider-header">
              <span class="ing-label"><Milk class="ing-icon text-amber" /> Manteiga</span>
              <div class="input-unit-wrapper">
                <input type="number" v-model.number="stocks.manteiga" min="0" max="100" class="num-input" />
                <span class="unit">kg</span>
              </div>
            </div>
            <input type="range" v-model.number="stocks.manteiga" min="0" max="100" class="range-slider" />
          </div>

          <!-- Cheese (Queijo) -->
          <div class="slider-row">
            <div class="slider-header">
              <span class="ing-label"><Pizza class="ing-icon text-yellow" /> Queijo</span>
              <div class="input-unit-wrapper">
                <input type="number" v-model.number="stocks.queijo" min="0" max="150" class="num-input" />
                <span class="unit">kg</span>
              </div>
            </div>
            <input type="range" v-model.number="stocks.queijo" min="0" max="150" class="range-slider" />
          </div>

          <!-- Sauce (Molho) -->
          <div class="slider-row">
            <div class="slider-header">
              <span class="ing-label"><Droplets class="ing-icon text-blue" /> Molho de Tomate</span>
              <div class="input-unit-wrapper">
                <input type="number" v-model.number="stocks.molho" min="0" max="500" class="num-input" />
                <span class="unit">kg</span>
              </div>
            </div>
            <input type="range" v-model.number="stocks.molho" min="0" max="500" class="range-slider" />
          </div>

          <!-- Calabresa -->
          <div class="slider-row">
            <div class="slider-header">
              <span class="ing-label"><Beef class="ing-icon text-red" /> Calabresa</span>
              <div class="input-unit-wrapper">
                <input type="number" v-model.number="stocks.calabresa" min="0" max="100" class="num-input" />
                <span class="unit">kg</span>
              </div>
            </div>
            <input type="range" v-model.number="stocks.calabresa" min="0" max="100" class="range-slider" />
          </div>
        </div>

        <!-- Recipe Configuration -->
        <div class="control-group">
          <h3 class="sub-group-title">Receitas & Lucros</h3>

          <!-- Pizza 1 (Muçarela) -->
          <div class="pizza-card-config">
            <div class="pizza-card-header">
              <Pizza class="pizza-icon text-amber" />
              <h4>Pizza 1: Muçarela</h4>
              <div class="profit-input-wrap">
                <span>Lucro Z1: $</span>
                <input type="number" v-model.number="profits.pizza1" min="1" max="100" class="num-input profit-input" />
              </div>
            </div>
            <div class="recipe-grid">
              <div class="recipe-item">
                <span>Farinha:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza1.farinha" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Manteiga:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza1.manteiga" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Queijo:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza1.queijo" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Molho:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza1.molho" class="num-input recipe-val" /> kg
              </div>
            </div>
          </div>

          <!-- Pizza 2 (Calabresa) -->
          <div class="pizza-card-config">
            <div class="pizza-card-header">
              <Pizza class="pizza-icon text-red" />
              <h4>Pizza 2: Calabresa</h4>
              <div class="profit-input-wrap">
                <span>Lucro Z2: $</span>
                <input type="number" v-model.number="profits.pizza2" min="1" max="100" class="num-input profit-input" />
              </div>
            </div>
            <div class="recipe-grid">
              <div class="recipe-item">
                <span>Farinha:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza2.farinha" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Manteiga:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza2.manteiga" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Queijo:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza2.queijo" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item">
                <span>Molho:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza2.molho" class="num-input recipe-val" /> kg
              </div>
              <div class="recipe-item double-col">
                <span>Calabresa:</span>
                <input type="number" step="0.05" v-model.number="recipes.pizza2.calabresa" class="num-input recipe-val" /> kg
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Main Panel: Results & Graphics -->
      <section class="results-panel">
        <!-- KPI Row -->


        <div class="kpi-grid">
          <div class="kpi-card border-blue">
            <div class="kpi-icon-wrapper blue-icon">
              <Pizza class="kpi-icon-svg" />
            </div>
            <div class="kpi-content">
              <h3>Produção Ótima</h3>
              <p class="kpi-value">{{ optimizeProductionTotal.toFixed(0) }}</p>
            </div>
          </div>
          <div class="kpi-card border-indigo">
            <div class="kpi-icon-wrapper indigo-icon">
              <DollarSign class="kpi-icon-svg" />
            </div>
            <div class="kpi-content">
              <h3>Lucro Estimado</h3>
              <p class="kpi-value">${{ optimizeResult.total_profit.toFixed(2) }}</p>
            </div>
          </div>
          <div class="kpi-card border-orange">
            <div class="kpi-icon-wrapper orange-icon">
              <AlertTriangle class="kpi-icon-svg" />
            </div>
            <div class="kpi-content">
              <h3>Gargalo do Estoque</h3>
              <p class="kpi-value" style="font-size:1rem; line-height:1.4;">{{ optimizationInventoryStatus }}</p>
            </div>
          </div>
          <div class="kpi-card border-green">
            <div class="kpi-icon-wrapper green-icon">
              <Activity class="kpi-icon-svg" />
            </div>
            <div class="kpi-content">
              <h3>Uso do Estoque</h3>
              <p class="kpi-value">{{ optimizeInventoryUsage.toFixed(1) }}%</p>
            </div>
          </div>
        </div>

        <section class="optimization-details glass-panel">
          <div class="optimization-details-header">
            <div>
              <h3 class="section-subtitle">Detalhes da Otimização</h3>
              <p class="info-desc">Use este painel para revisar o plano de produção ideal, o estoque restante e os gargalos após otimização.</p>
            </div>
            <button class="primary-btn" @click="runOptimization" :disabled="optimizationLoading">
              {{ optimizationLoading ? 'Calculando...' : 'Atualizar Otimização' }}
            </button>
          </div>

          <div class="optimization-details-body">
            <div v-if="optimizationLoading" class="info-desc">Conectando-se à API e calculando o plano ótimo...</div>

            <div v-else-if="optimizeResult.success">
              <div class="details-grid">
                <div class="detail-block">
                  <h4>Plano de Produção</h4>
                  <ul>
                    <li v-for="(qty, pizza) in optimizeResult.production_plan" :key="pizza">
                      <strong>{{ pizzaName(pizza) }}</strong>: {{ qty }} pizzas
                    </li>
                  </ul>
                </div>
                <div class="consumption-wrapper glass-panel">
                  <h4>Estoque Restante</h4>
                  <ul>
                    <li v-for="(qty, ing) in optimizeResult.remaining_inventory" :key="ing">
                      <strong>{{ getIngName(ing) }}</strong>: {{ qty.toFixed(2) }} kg
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div v-else-if="optimizeResult.message" class="alert-box">
              {{ optimizeResult.message }}
            </div>

            <div v-else class="info-desc">
              Clique em "Atualizar Otimização" para gerar o plano de produção mais lucrativo.
            </div>
          </div>
        </section>

        <!-- Visualization Row -->
        <div class="visuals-grid">
          <!-- Manual Simulation Controls -->
          <div class="simple-info-wrapper glass-panel">
            <h3 class="section-subtitle"><Activity class="subtitle-icon text-green" /> Produção de Pizzas</h3>
            <div class="simple-viz-body">
              <div class="production-panel">
                <div class="production-grid">
                  <div class="field-group">
                    <label class="field-label" for="pizza-type">Tipo de Pizza</label>
                    <select id="pizza-type" v-model="production.pizza" class="select-input">
                      <option value="pizza1">Pizza Muçarela</option>
                      <option value="pizza2">Pizza Calabresa</option>
                    </select>
                  </div>

                  <div class="field-group">
                    <label class="field-label" for="production-qty">Quantidade</label>
                    <div class="input-unit-wrapper quantity-field">
                      <input
                        id="production-qty"
                        type="number"
                        v-model.number="production.quantity"
                        min="1"
                        step="1"
                        @change="production.quantity = Math.max(1, Math.floor(production.quantity))"
                        @blur="production.quantity = Math.max(1, Math.floor(production.quantity))"
                        class="num-input quantity-input"
                      />
                      <span class="unit">pizzas</span>
                    </div>
                  </div>

                  <div class="button-group">
                    <button class="primary-btn" @click="producePizza" :disabled="!productionSufficient || production.quantity <= 0">
                      Produzir
                    </button>
                    <p class="helper-text">Produção aplicada automaticamente ao clicar.</p>
                  </div>
                </div>

                <div class="production-preview">
                  <p class="info-desc">
                    Preview de consumo antes de confirmar. Ingredientes serão deduzidos do estoque ao concluir a produção.
                  </p>

                  <div class="preview-list">
                    <div v-for="(item, key) in productionPreview" :key="key" class="preview-row">
                      <span>{{ getIngName(key) }}</span>
                      <span class="preview-value">
                        {{ item.required.toFixed(2) }}kg
                        <small class="preview-stock">/ {{ item.stock.toFixed(2) }}kg disponível</small>
                      </span>
                    </div>
                  </div>

                  <div v-if="productionErrors.length" class="alert-box">
                    <strong>Estoque insuficiente:</strong>
                    <ul>
                      <li v-for="item in productionErrors" :key="item.ing">
                        {{ getIngName(item.ing) }}: faltam {{ item.missing.toFixed(2) }}kg
                      </li>
                    </ul>
                  </div>

                  <div v-if="successMessage" class="success-box">
                    {{ successMessage }}
                  </div>

                  <div class="history-table-wrapper">
                    <h4 class="history-title">Histórico de Produção</h4>
                    <div v-if="productionHistory.length === 0" class="info-desc">Nenhuma produção registrada ainda.</div>
                    <table v-else class="history-table">
                      <thead>
                        <tr>
                          <th>Data / Hora</th>
                          <th>Pizza</th>
                          <th>Quantidade</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="entry in productionHistory" :key="entry.id">
                          <td>{{ successTimestamp(entry.timestamp) }}</td>
                          <td>{{ pizzaName(entry.pizza) }}</td>
                          <td>{{ entry.quantity }}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>
    </main>
  </div>
</template>

<script>
import { ref, reactive, computed } from 'vue';
import { 
  Pizza, 
  Sliders, 
  Wheat, 
  Milk, 
  Droplets, 
  Beef, 
  DollarSign, 
  AlertTriangle, 
  Activity, 
  AlertCircle 
} from '@lucide/vue';

export default {
  name: 'App',
  components: {
    Pizza,
    Sliders,
    Wheat,
    Milk,
    Droplets,
    Beef,
    DollarSign,
    AlertTriangle,
    Activity,
    AlertCircle
  },
  setup() {
    // Manual simulation pizza quantities
    const simQty = reactive({
      pizza1: 50,
      pizza2: 50
    });

    const production = reactive({
      pizza: 'pizza1',
      quantity: 1
    });

    const productionHistory = ref([]);
    const successMessage = ref('');
    const optimizationLoading = ref(false);
    const optimizeResult = reactive({
      success: false,
      production_plan: {},
      total_profit: 0,
      remaining_inventory: {},
      bottleneck_ingredients: [],
      message: ''
    });

    // Stocks available (initial values)
    const stocks = reactive({
      farinha: 150,
      manteiga: 25,
      queijo: 50,
      molho: 160,
      calabresa: 30
    });

    // Recipes (how much of each ingredient is required per pizza)
    const recipes = reactive({
      pizza1: { // Muçarela
        farinha: 0.5,
        manteiga: 0.2,
        queijo: 0.3,
        molho: 0.2,
        calabresa: 0.0
      },
      pizza2: { // Calabresa
        farinha: 0.5,
        manteiga: 0.2,
        queijo: 0.2,
        molho: 0.2,
        calabresa: 0.15
      }
    });

    // Profit per unit of pizza
    const profits = reactive({
      pizza1: 12.00,
      pizza2: 15.00
    });

    const simProfit = computed(() => {
      return (simQty.pizza1 * profits.pizza1) + (simQty.pizza2 * profits.pizza2);
    });

    const simUsage = computed(() => {
      const usage = {};
      for (const [ing, stock] of Object.entries(stocks)) {
        const req1 = recipes.pizza1[ing] || 0;
        const req2 = recipes.pizza2[ing] || 0;
        const used = (req1 * simQty.pizza1) + (req2 * simQty.pizza2);
        const leftover = stock - used;
        const percent = stock > 0 ? (used / stock) * 100 : 0;
        
        usage[ing] = {
          used: Math.max(0.0, used),
          stock: stock,
          percent: Math.min(100.0, percent),
          rawPercent: percent,
          leftover: leftover,
          bottleneck: percent >= 99.9,
          insufficient: leftover < 0
        };
      }
      return usage;
    });

    const activeProfit = computed(() => simProfit.value);

    const productionPreview = computed(() => {
      const recipe = recipes[production.pizza] || {};
      const quantity = Math.max(0, Math.floor(Number(production.quantity) || 0));
      const preview = {};
      for (const [ing, stock] of Object.entries(stocks)) {
        const requiredPerUnit = recipe[ing] || 0;
        const required = Number((requiredPerUnit * quantity).toFixed(2));
        const leftover = Number((stock - required).toFixed(2));

        preview[ing] = {
          required,
          stock,
          leftover,
          insufficient: leftover < 0
        };
      }
      return preview;
    });

    const productionErrors = computed(() => {
      return Object.entries(productionPreview.value)
        .filter(([_, item]) => item.insufficient)
        .map(([ing, item]) => ({
          ing,
          missing: Math.abs(item.leftover)
        }));
    });

    const productionSufficient = computed(() => {
      return production.quantity > 0 && productionErrors.value.length === 0;
    });

    const productionTotal = computed(() => productionHistory.value.length);

    const successTimestamp = (date) => {
      return new Date(date).toLocaleString('pt-BR', {
        dateStyle: 'short',
        timeStyle: 'short'
      });
    };

    const pizzaName = (key) => {
      return key === 'pizza2' ? 'Pizza Calabresa' : 'Pizza Muçarela';
    };

    const producePizza = () => {
      const quantity = Math.max(0, Math.floor(Number(production.quantity) || 0));
      production.quantity = quantity;
      if (quantity <= 0) {
        successMessage.value = '';
        return;
      }

      if (!productionSufficient.value) {
        successMessage.value = '';
        return;
      }

      const pizzaLabel = pizzaName(production.pizza);
      // Deduct inventory and record history without browser confirmation popup
      const consumed = {};
      for (const [ing, item] of Object.entries(productionPreview.value)) {
        consumed[ing] = item.required;
        stocks[ing] = Number(Math.max(0, stocks[ing] - item.required).toFixed(2));
      }

      productionHistory.value.unshift({
        id: Date.now(),
        timestamp: new Date().toISOString(),
        pizza: production.pizza,
        quantity,
        consumed
      });

      successMessage.value = `Produção de ${quantity} ${pizzaLabel} concluída. Estoque atualizado.`;
      setTimeout(() => {
        successMessage.value = '';
      }, 5000);
    };

    const runOptimization = async () => {
      optimizationLoading.value = true;
      optimizeResult.success = false;
      optimizeResult.message = '';

      try {
        const response = await fetch('/api/solve', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            mode: 'optimize',
            stocks,
            recipes,
            profits
          })
        });

        const data = await response.json();
        if (!response.ok || data.success === false) {
          throw new Error(data.message || 'Falha ao calcular otimização.');
        }

        optimizeResult.success = true;
        const normalizedPlan = {};
        for (const [pizza, qty] of Object.entries(data.production_plan || {})) {
          normalizedPlan[pizza] = Math.max(0, Math.floor(Number(qty) || 0));
        }
        optimizeResult.production_plan = normalizedPlan;
        optimizeResult.total_profit = data.total_profit || 0;
        optimizeResult.remaining_inventory = data.remaining_inventory || {};
        optimizeResult.bottleneck_ingredients = data.bottleneck_ingredients || [];
        optimizeResult.message = '';
      } catch (error) {
        optimizeResult.success = false;
        optimizeResult.message = error.message || 'Falha ao calcular otimização.';
      } finally {
        optimizationLoading.value = false;
      }
    };

    const isLastConsumed = (consumed, key) => {
      const entries = Object.entries(consumed).filter(([_, amount]) => amount > 0);
      return entries.length > 0 && entries[entries.length - 1][0] === key;
    };

    const activeUsage = computed(() => {
      const adapted = {};
      for (const [ing, data] of Object.entries(simUsage.value)) {
        adapted[ing] = {
          ...data,
          leftover: data.leftover,
          rawPercent: data.percent,
          insufficient: data.insufficient
        };
      }
      return adapted;
    });

    const stockEfficiency = computed(() => {
      let totalPercent = 0;
      let count = 0;
      Object.values(simUsage.value).forEach(data => {
        totalPercent += data.percent;
        count++;
      });
      return (totalPercent / count).toFixed(1);
    });

    const kpiStatusClass = computed(() => {
      const hasInsufficient = Object.values(simUsage.value).some(u => u.insufficient);
      return hasInsufficient ? 'border-orange bg-red-opaque' : 'border-slate';
    });

    const kpiStatusIconClass = computed(() => {
      const hasInsufficient = Object.values(simUsage.value).some(u => u.insufficient);
      return hasInsufficient ? 'red-icon' : 'green-icon';
    });

    const kpiStatusText = computed(() => {
      const insufficients = Object.entries(simUsage.value)
        .filter(([_, u]) => u.insufficient)
        .map(([ing, _]) => getIngName(ing));
      if (insufficients.length > 0) {
        return 'Falta: ' + insufficients.join(', ');
      }
      return 'Suficiente';
    });

    const kpiStatusTextClass = computed(() => {
      const hasInsufficient = Object.values(simUsage.value).some(u => u.insufficient);
      return hasInsufficient ? 'text-red font-bold font-sm' : 'text-green font-bold';
    });

    const optimizeProductionTotal = computed(() => {
      return Object.values(optimizeResult.production_plan || {}).reduce((sum, qty) => sum + (Number(qty) || 0), 0);
    });

    const optimizeInventoryUsage = computed(() => {
      const remaining = optimizeResult.remaining_inventory || {};
      const keys = Object.keys(remaining);
      if (!keys.length) return 0;
      const usagePercents = keys.map((ing) => {
        const stock = stocks[ing] ?? 0;
        if (stock <= 0) return 0;
        const used = stock - Number(remaining[ing] || 0);
        return Math.min(100, Math.max(0, (used / stock) * 100));
      });
      return usagePercents.reduce((sum, value) => sum + value, 0) / usagePercents.length;
    });

    const optimizationInventoryStatus = computed(() => {
      if (optimizeResult.bottleneck_ingredients?.length) {
        return optimizeResult.bottleneck_ingredients.map(getIngName).join(', ');
      }
      if (optimizeResult.success) {
        return 'Estoque suficiente';
      }
      return 'Aguardando cálculo';
    });

    const getIngIconComponent = (key) => {
      const icons = {
        farinha: 'Wheat',
        manteiga: 'Milk',
        queijo: 'Pizza',
        molho: 'Droplets',
        calabresa: 'Beef'
      };
      return icons[key] || 'Pizza';
    };

    const getIngName = (key) => {
      const names = {
        farinha: 'Farinha',
        manteiga: 'Manteiga',
        queijo: 'Queijo',
        molho: 'Molho de Tomate',
        calabresa: 'Calabresa'
      };
      return names[key] || key;
    };

    return {
      stocks,
      recipes,
      profits,
      simQty,
      production,
      productionHistory,
      productionPreview,
      productionErrors,
      productionSufficient,
      successMessage,
      stockEfficiency,
      getIngIconComponent,
      getIngName,
      activeProfit,
      activeUsage,
      kpiStatusClass,
      kpiStatusIconClass,
      kpiStatusText,
      kpiStatusTextClass,
      pizzaName,
      producePizza,
      successTimestamp,
      isLastConsumed,
      optimizeResult,
      optimizationLoading,
      optimizeProductionTotal,
      optimizeInventoryUsage,
      optimizationInventoryStatus,
      runOptimization
    };
  }
};
</script>
\n\n<style>
/* Global resets & typography */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: #060913;
  background-image: 
    radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.1) 0px, transparent 50%),
    radial-gradient(at 50% 0%, rgba(59, 130, 246, 0.05) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.05) 0px, transparent 50%);
  background-attachment: fixed;
  color: #f1f5f9;
  font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  line-height: 1.5;
}

.font-mono {
  font-family: 'JetBrains Mono', monospace;
}

/* Dashboard Layout Wrapper */
.dashboard-wrapper {
  max-width: 1600px;
  margin: 0 auto;
  padding: 28px 24px;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

/* Header */
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 28px;
  background: rgba(13, 20, 38, 0.6);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 18px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
}

.logo-area {
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo-icon {
  width: 36px;
  height: 36px;
  color: #ef4444;
  filter: drop-shadow(0 0 8px rgba(239, 68, 68, 0.4));
  animation: logo-spin 20s linear infinite;
}

@keyframes logo-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.logo-text h1 {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #60a5fa 0%, #818cf8 50%, #c084fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.logo-text p {
  font-size: 0.85rem;
  color: #94a3b8;
}

.header-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.2);
  color: #34d399;
  padding: 6px 14px;
  border-radius: 30px;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.3px;
  box-shadow: 0 2px 10px rgba(16, 185, 129, 0.05);
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-dot.green {
  background-color: #10b981;
  box-shadow: 0 0 10px #10b981;
}

.pulse-glow {
  animation: pulse-dot 2s infinite ease-in-out;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 0.7; transform: scale(0.95); }
  50% { opacity: 1; transform: scale(1.15); box-shadow: 0 0 14px #10b981; }
}

/* Grid Layout */
.dashboard-grid {
  display: grid;
  grid-template-columns: 390px 1fr;
  gap: 28px;
}

@media (max-width: 1200px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

/* Glassmorphism Panels */
.glass-panel {
  background: rgba(13, 20, 38, 0.5);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  padding: 26px;
  height: fit-content;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
  transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
}

.glass-panel:hover {
  border-color: rgba(99, 102, 241, 0.15);
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.5);
}

.panel-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 24px;
  color: #f8fafc;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  padding-bottom: 14px;
  letter-spacing: 0.2px;
}

/* Form groups and control layout */
.control-group {
  margin-bottom: 26px;
}

.group-label {
  display: block;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 12px;
}

.sub-group-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: #cbd5e1;
  margin-bottom: 18px;
  border-left: 3px solid #6366f1;
  padding-left: 10px;
  letter-spacing: 0.2px;
}

.optimization-panel {
  margin-bottom: 24px;
}

.optimization-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 18px;
}

.optimization-header h3 {
  margin-bottom: 8px;
}

.optimization-results {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.result-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.result-card,
.result-block {
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 18px;
}

.result-card .result-label,
.result-block h4 {
  font-size: 0.85rem;
  color: #94a3b8;
  margin-bottom: 10px;
}

.result-card .result-value {
  display: block;
  font-size: 2rem;
  margin-top: 6px;
  color: #f8fafc;
}

.result-text {
  color: #cbd5e1;
  line-height: 1.6;
}

.result-block ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.result-block li {
  font-size: 0.95rem;
  margin-bottom: 8px;
  color: #e2e8f0;
}

@media (max-width: 900px) {
  .result-row {
    grid-template-columns: 1fr;
  }
}

/* Mode Tabs Selector */
.mode-tabs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  background: rgba(6, 9, 22, 0.6);
  padding: 6px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.04);
}

.tab-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: transparent;
  border: none;
  color: #94a3b8;
  padding: 10px 14px;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
}

.tab-btn:hover {
  color: #f1f5f9;
  background: rgba(255, 255, 255, 0.03);
}

.tab-btn.active {
  background: #6366f1;
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35);
}

.btn-icon {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
}

/* Preset buttons style */
.preset-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.preset-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(30, 41, 59, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.05);
  color: #cbd5e1;
  padding: 12px 16px;
  font-size: 0.85rem;
  font-weight: 500;
  border-radius: 10px;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
  font-family: inherit;
  width: 100%;
}

.preset-btn:hover {
  background: rgba(99, 102, 241, 0.08);
  border-color: rgba(99, 102, 241, 0.3);
  color: #ffffff;
  transform: translateX(2px);
}

/* Sliders Styling */
.slider-row {
  margin-bottom: 20px;
  background: rgba(255, 255, 255, 0.01);
  border: 1px solid rgba(255, 255, 255, 0.02);
  padding: 12px 14px;
  border-radius: 12px;
}

.slider-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.ing-label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #cbd5e1;
}

.ing-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.input-unit-wrapper {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  background: rgba(6, 9, 22, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 8px 12px;
  transition: border-color 0.2s ease;
  gap: 10px;
}

.input-unit-wrapper:focus-within {
  border-color: #6366f1;
}

.quantity-field {
  min-width: 0;
}

.num-input {
  background: transparent;
  border: none;
  color: #f8fafc;
  width: 80px;
  min-width: 60px;
  font-size: 0.95rem;
  font-family: 'JetBrains Mono', monospace;
  text-align: right;
  outline: none;
  padding: 8px 8px 8px 4px;
}

.quantity-input {
  padding-right: 12px;
}

.unit {
  font-size: 0.8rem;
  color: #94a3b8;
  margin-left: 10px;
  font-weight: 600;
}

.range-slider {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 3px;
  outline: none;
  display: block;
}

.range-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 14px;
  height: 14px;
  background: #ffffff;
  border: 2.5px solid #6366f1;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(99, 102, 241, 0.8);
  transition: transform 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color 0.15s ease;
}

.range-slider::-webkit-slider-thumb:hover {
  transform: scale(1.3);
  border-color: #818cf8;
}

/* Pizza Card Configuration */
.pizza-card-config {
  background: rgba(13, 20, 38, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 14px;
  padding: 16px;
  margin-top: 16px;
  transition: border-color 0.2s ease;
}

.pizza-card-config:hover {
  border-color: rgba(255, 255, 255, 0.08);
}

.pizza-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.pizza-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

.pizza-card-header h4 {
  font-size: 0.9rem;
  font-weight: 700;
  color: #f1f5f9;
  flex: 1;
}

.profit-input-wrap {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 0.8rem;
  color: #64748b;
}

.profit-input {
  width: 50px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(6, 9, 22, 0.4);
  border-radius: 6px;
  padding: 2px 4px;
  font-size: 0.85rem;
}

.recipe-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.recipe-item {
  font-size: 0.75rem;
  color: #94a3b8;
  display: flex;
  align-items: center;
  gap: 6px;
}

.recipe-val {
  width: 44px;
  padding: 2px;
  font-size: 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(6, 9, 22, 0.4);
  border-radius: 6px;
}

.double-col {
  grid-column: span 2;
}

/* Right Panel: Results */
.results-panel {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

/* KPIs Dashboard */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.kpi-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

.kpi-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
}

.border-green::after { background: #10b981; }
.border-indigo::after { background: #6366f1; }
.border-orange::after { background: #f97316; }
.border-blue::after { background: #3b82f6; }
.border-slate::after { background: #475569; }

.kpi-icon-wrapper {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.kpi-icon-svg {
  width: 20px;
  height: 20px;
}

.green-icon { background: rgba(16, 185, 129, 0.08); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.15); }
.indigo-icon { background: rgba(99, 102, 241, 0.08); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.15); }
.orange-icon { background: rgba(249, 115, 22, 0.08); color: #fb923c; border: 1px solid rgba(249, 115, 22, 0.15); }
.blue-icon { background: rgba(59, 130, 246, 0.08); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.15); }
.slate-icon { background: rgba(71, 85, 105, 0.08); color: #94a3b8; border: 1px solid rgba(71, 85, 105, 0.15); }

.optimization-details {
  padding: 24px;
}

.optimization-details-header {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: flex-start;
  margin-bottom: 20px;
}

.optimization-details-header .primary-btn {
  height: 42px;
}

.optimization-details-body {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.detail-block {
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 18px;
  padding: 18px;
}

.detail-block.full-width {
  grid-column: 1 / -1;
}

.detail-block h4 {
  margin-bottom: 10px;
  color: #cbd5e1;
  font-size: 0.95rem;
}

.detail-block ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.detail-block li {
  margin-bottom: 10px;
  color: #e2e8f0;
}

.kpi-content h3 {
  font-size: 0.75rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 6px;
}

.kpi-value {
  font-size: 1.3rem;
  font-weight: 700;
  color: #f8fafc;
}

.kpi-qty-flex {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.flex-center {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.inline-icon {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}

.math-operator {
  color: #475569;
  font-size: 1rem;
  font-weight: 400;
}

.total-qty {
  font-size: 0.95rem;
  color: #94a3b8;
  margin-left: 2px;
}

.sub-qty {
  font-size: 1.15rem;
}

.text-amber { color: #fbbf24; }
.text-red { color: #f43f5e; }
.text-yellow { color: #f59e0b; }
.text-blue { color: #3b82f6; }
.text-indigo { color: #818cf8; }
.text-orange { color: #f97316; }
.text-green { color: #10b981; }

.bg-red-opaque {
  background: rgba(244, 63, 94, 0.06) !important;
}

/* Visuals Layout */
.visuals-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 28px;
}

@media (max-width: 1000px) {
  .visuals-grid {
    grid-template-columns: 1fr;
  }
}

.chart-wrapper {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.section-subtitle {
  display: flex;
  align-items: center;
  font-size: 1.05rem;
  font-weight: 700;
  color: #cbd5e1;
  letter-spacing: 0.2px;
}

.subtitle-icon {
  width: 18px;
  height: 18px;
  margin-right: 8px;
  flex-shrink: 0;
}

.chart-inner {
  flex: 1;
  position: relative;
  min-height: 400px;
}

/* Informative simple viz panel */
.simple-info-wrapper {
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: rgba(13, 20, 38, 0.3);
}

.simple-viz-body {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.info-desc {
  font-size: 0.85rem;
  color: #94a3b8;
  line-height: 1.6;
}

.limit-cards-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.limit-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  background: rgba(30, 41, 59, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 12px;
  position: relative;
  transition: all 0.2s ease;
}

.limit-card:hover {
  background: rgba(30, 41, 59, 0.2);
  border-color: rgba(255, 255, 255, 0.06);
}

.limit-icon-wrapper {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.limit-icon-svg {
  width: 18px;
  height: 18px;
}

.limit-details h4 {
  font-size: 0.85rem;
  font-weight: 700;
  color: #cbd5e1;
  margin-bottom: 2px;
}

.limit-calc {
  font-size: 0.75rem;
  color: #64748b;
  margin-bottom: 2px;
}

.limit-value {
  font-size: 0.85rem;
  color: #94a3b8;
}

.limit-value strong {
  color: #f1f5f9;
}

.limit-bottleneck {
  border-color: rgba(249, 115, 22, 0.25);
  background: rgba(249, 115, 22, 0.04);
}

.limit-bottleneck:hover {
  background: rgba(249, 115, 22, 0.06);
  border-color: rgba(249, 115, 22, 0.35);
}

.limit-bottleneck .limit-value strong {
  color: #fb923c;
}

.bottleneck-tag {
  position: absolute;
  right: 14px;
  top: 14px;
  font-size: 0.65rem;
  font-weight: 800;
  background: #f97316;
  color: #ffffff;
  padding: 3px 8px;
  border-radius: 6px;
  letter-spacing: 0.5px;
}

.badge-pulse {
  animation: badge-pulse-anim 2s infinite ease-in-out;
}

@keyframes badge-pulse-anim {
  0%, 100% { opacity: 0.9; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.05); box-shadow: 0 0 10px rgba(249, 115, 22, 0.4); }
}

.production-panel {
  margin-top: 24px;
  background: rgba(30, 41, 59, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 18px;
  padding: 20px;
}

.production-grid {
  display: grid;
  grid-template-columns: minmax(200px, 1.2fr) minmax(180px, 1fr) minmax(180px, 0.8fr);
  gap: 18px;
  align-items: end;
}

.field-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.button-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  gap: 8px;
}

.select-input {
  background: rgba(6, 9, 22, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  color: #f8fafc;
  padding: 12px 14px;
  font-size: 0.95rem;
}

.helper-text {
  color: #94a3b8;
  font-size: 0.78rem;
  line-height: 1.4;
  max-width: 220px;
}

@media (max-width: 820px) {
  .production-grid {
    grid-template-columns: 1fr;
  }

  .button-group {
    align-items: stretch;
  }

  .primary-btn {
    width: 100%;
  }
}

.primary-btn {
  background: #6366f1;
  color: #ffffff;
  border: none;
  border-radius: 12px;
  padding: 14px 18px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.2s ease;
}

.primary-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.primary-btn:hover:not(:disabled) {
  background: #818cf8;
  transform: translateY(-1px);
}

.production-preview {
  margin-top: 18px;
  display: grid;
  gap: 14px;
}

.preview-list {
  display: grid;
  gap: 10px;
}

.preview-row {
  display: flex;
  justify-content: space-between;
  padding: 12px 14px;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 12px;
  color: #e2e8f0;
}

.preview-value {
  text-align: right;
  font-weight: 700;
}

.preview-stock {
  display: block;
  font-size: 0.72rem;
  color: #94a3b8;
}

.alert-box,
.success-box {
  border-radius: 14px;
  padding: 14px 16px;
  font-size: 0.88rem;
}

.alert-box {
  background: rgba(248, 113, 113, 0.14);
  border: 1px solid rgba(248, 113, 113, 0.25);
  color: #fee2e2;
}

.success-box {
  background: rgba(34, 197, 94, 0.12);
  border: 1px solid rgba(34, 197, 94, 0.25);
  color: #dcfce7;
}

.history-table-wrapper {
  margin-top: 18px;
}

.history-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 10px;
  color: #f8fafc;
}

.history-table th,
.history-table td {
  white-space: nowrap;
}

@media (max-width: 720px) {
  .history-table th,
  .history-table td {
    padding: 10px 8px;
    font-size: 0.78rem;
  }
}

.history-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.8rem;
}

.history-table th,
.history-table td {
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 10px 12px;
  text-align: left;
}

.history-table th {
  color: #94a3b8;
  background: rgba(255, 255, 255, 0.03);
}

.history-table td {
  color: #e2e8f0;
}

/* Consumption Progress section */
.consumption-wrapper {
  display: flex;
  flex-direction: column;
  gap: 18px;
  width: 350px;
  height: fit-content;
}

.optimization-details .consumption-wrapper {
  width: 100%;
}

.progress-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.progress-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  align-items: center;
}

.progress-label {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: #cbd5e1;
}

.progress-icon-svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
}

.progress-numerical {
  color: #94a3b8;
}

.bar-container {
  height: 6px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 4px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 4px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.bg-normal { background: linear-gradient(90deg, #6366f1, #3b82f6); }
.bg-warning { background: linear-gradient(90deg, #f59e0b, #f97316); }
.bg-red { background: linear-gradient(90deg, #ef4444, #f43f5e); box-shadow: 0 0 8px rgba(244, 63, 94, 0.3); }

.progress-footer {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  align-items: center;
}

.percentage {
  color: #64748b;
  font-weight: 600;
}

.text-red {
  color: #f87171;
}

.text-green {
  color: #34d399;
}

.leftover-text {
  color: #34d399;
  font-size: 0.75rem;
  font-weight: 600;
}

.simulation-sliders {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 10px;
}

.alert-icon-inline {
  width: 12px;
  height: 12px;
  margin-right: 4px;
  flex-shrink: 0;
}

.text-flex-align {
  display: inline-flex;
  align-items: center;
}

.gargalo-indicator-text {
  color: #fb923c;
  font-weight: 700;
}

.target-select-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px;
  background: rgba(6, 9, 22, 0.5);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.04);
  margin-top: 8px;
}

.target-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  background: transparent;
  border: none;
  color: #94a3b8;
  padding: 8px 6px;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
}

.target-btn:hover {
  color: #f1f5f9;
  background: rgba(255, 255, 255, 0.02);
}

.target-btn.active {
  background: #6366f1;
  color: #ffffff;
  box-shadow: 0 2px 10px rgba(99, 102, 241, 0.3);
}

@keyframes pulse-warn {
  0%, 100% { opacity: 0.85; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.02); }
}

/* Animations */
.animate-fade-in {
  animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
