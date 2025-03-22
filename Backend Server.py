from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('smart_dustbin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS waste_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fill_level INTEGER,
            temperature REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    fill_level = data.get('fill_level')
    temperature = data.get('temperature')

    conn = sqlite3.connect('smart_dustbin.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO waste_data (fill_level, temperature) VALUES (?, ?)', (fill_level, temperature))
    conn.commit()
    conn.close()
    return jsonify({"message": "Data updated successfully"}), 200

@app.route('/data', methods=['GET'])
def fetch_data():
    conn = sqlite3.connect('smart_dustbin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM waste_data ORDER BY timestamp DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
