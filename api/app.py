from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'tpdb'),
        user=os.getenv('POSTGRES_USER', 'tpuser'),
        password=os.getenv('POSTGRES_PASSWORD', 'tppass'),
        host='db'
    )
    return conn

@app.route('/')
def home():
    return 'API Python et PostgreSQL opérationnelle'

@app.route('/products')
def products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, price FROM products ORDER BY id;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': r[0], 'name': r[1], 'price': float(r[2])} for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

