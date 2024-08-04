from flask import Blueprint, request, render_template, jsonify
from src.core.searcher import Searcher

api = Blueprint('api', __name__)

@api.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = api.searcher.search(query)
    return render_template('results.html', results=results.to_dict('records'))

@api.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('query', '')
    results = api.searcher.search(query)
    return jsonify(results.to_dict('records'))