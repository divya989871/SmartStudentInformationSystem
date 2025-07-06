from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (data['username'], data['password']))
    result = cur.fetchone()
    return jsonify({"status": "success" if result else "fail"})

@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    return jsonify(data)

app.run(debug=True)