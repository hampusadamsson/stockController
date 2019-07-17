import json
import os
from flask import Flask
from flask_cors import CORS

from Data_manager import get_stock, get_distinct_stocks, get_stock_at_date

app = Flask(__name__)
CORS(app)
# filename = os.path.join(app.root_path, 'resources', 'stocks.db')
filename = os.environ['STOCKDB']
print(filename)

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


@app.route('/getStockAtDate/<symbol>/<date>/<days_limit>')
def cntrl_get_stock_at_date(symbol, date, days_limit):
    df = get_stock_at_date(filename, symbol, date, days_limit)
    return df.to_json()


app.run(host="0.0.0.0")

