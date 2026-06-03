from pathlib import Path
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.solver import solve_1d, solve_2d, solve_multivariable

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIST = BASE_DIR / 'dist'

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIST),
    static_url_path=''
)
CORS(app, resources={r'/api/*': {'origins': '*'}})

@app.route('/api/solve', methods=['POST'])
def solve():
    try:
        data = request.json or {}
        mode = data.get('mode', 'simple')
        stocks = data.get('stocks', {})
        recipes = data.get('recipes', {})
        profits = data.get('profits', {})

        clean_stocks = {k: float(v) for k, v in stocks.items()}

        clean_recipes = {}
        for pizza, ing_recipe in recipes.items():
            clean_recipes[pizza] = {k: float(v) for k, v in ing_recipe.items()}

        clean_profits = {k: float(v) for k, v in profits.items()}

        if mode in ('simple', 'pizza1'):
            result = solve_1d(
                stocks=clean_stocks,
                recipe=clean_recipes.get('pizza1', {}),
                profit=clean_profits.get('pizza1', 12.0)
            )
        elif mode == 'pizza2':
            result = solve_1d(
                stocks=clean_stocks,
                recipe=clean_recipes.get('pizza2', {}),
                profit=clean_profits.get('pizza2', 15.0),
                pizza_var='x2'
            )
        elif mode == 'mix':
            result = solve_2d(
                stocks=clean_stocks,
                recipes=clean_recipes,
                profits=clean_profits
            )
        elif mode == 'optimize':
            # General multi-variable optimization
            result = solve_multivariable(
                stocks=clean_stocks,
                recipes=clean_recipes,
                profits=clean_profits
            )
        else:
            return jsonify({
                'success': False,
                'message': f"Modo '{mode}' inválido."
            }), 400

        return jsonify(result)

    except ValueError as ve:
        return jsonify({
            'success': False,
            'message': f"Erro de conversão numérica: {str(ve)}"
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f"Ocorreu um erro no servidor: {str(e)}"
        }), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_spa(path):
    if path != '' and (FRONTEND_DIST / path).exists():
        return app.send_static_file(path)

    if (FRONTEND_DIST / 'index.html').exists():
        return app.send_static_file('index.html')

    return jsonify({
        'success': False,
        'message': 'Frontend não está compilado. Execute a construção do Vite antes de iniciar o servidor.'
    }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
