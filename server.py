from flask import Flask, render_template, request, jsonify
import sqlite3, time

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    return "Hello, this is your Flask server!"

@app.route('/slow-response')
def slow_response():
    time.sleep(5)  # Delays the response for 5 seconds
    return "This endpoint is 5 seconds slower!"

@app.route('/data')
def data_endpoint():
    return jsonify({
        "name": "John",
        "age": 30,
        "city": "New York"
    })

@app.route('/index.html')
def index():
    return render_template('index.html')  # Index template

@app.route('/search', methods=['POST'])
def search():
    name_query = request.form.get('name')
    
    # Connect to the SQLite database
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    cur = conn.cursor()

    # Query the database
    cur.execute("SELECT * FROM users WHERE username LIKE ?", ('%' + name_query + '%',))
    rows = cur.fetchall()

    # Convert row objects to dictionary
    records = [dict(row) for row in rows]

    # Close connection
    conn.close()
    
    # Return results as JSON
    return jsonify(records)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
