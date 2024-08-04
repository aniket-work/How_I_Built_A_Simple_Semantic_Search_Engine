from flask import Flask, render_template
from src.rest.api import api
from src.utils.data_loader import load_data
from src.core.indexer import Indexer
from src.core.searcher import Searcher
import json

app = Flask(__name__, template_folder='templates')

with open('config/config.json', 'r') as f:
    config = json.load(f)

df = load_data(config)
indexer = Indexer(config)
index, vectors = indexer.create_or_load_index(df)
searcher = Searcher(config, index, df)

api.searcher = searcher
app.register_blueprint(api)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(**config['flask'])