import json
import os
from flask import Flask
from flask_cors import CORS

from Data_manager import get_stock, get_distinct_stocks

app = Flask(__name__)
CORS(app)
filename = os.path.join(app.root_path, 'resources', 'stocks.db')


@app.route('/health')
def health():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/getDistinct')
def ctrl_get_distinct_stocks():
    df = get_distinct_stocks(filename)
    return df.to_json()


@app.route('/getStock/<symbol>')
def cntrl_get_stock(symbol):
    df = get_stock(filename, symbol, 100000)
    return df.to_json()


@app.route('/getStock/<symbol>/<days_limit>')
def cntrl_get_stock_last_days(symbol, days_limit):
    df = get_stock(filename, symbol, days_limit)
    return df.to_json()


if __name__ == '__main__':
    app.run(host="0.0.0.0")

