import sqlite3
import pandas as pd


def query(src, q):
    with sqlite3.connect(src) as conn:
        return pd.read_sql_query(q, conn)


def get_stock(src, symbol, limit=10):
    return query(src, "SELECT * FROM stocks WHERE symbol == '{}' ORDER BY date DESC LIMIT '{}';".format(symbol, limit))


def get_stock_at_date(src, symbol, date, days_limit):
    return query(src, "SELECT * FROM stocks WHERE symbol == '{}' AND date <= '{}' ORDER BY date DESC LIMIT '{}';".format(symbol, date, days_limit))


def get_distinct_stocks(src):
    return query(src, "SELECT DISTINCT symbol FROM stocks;")

