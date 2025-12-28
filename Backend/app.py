from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)  # allow frontend to talk to backend

@app.route("/")
def home():
    return "Backend is running successfully!"

# Database connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
	database="cipher_sql_studio",
        password="fuckboys12@",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/execute", methods=["POST"])
def execute_query():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"message": "Query cannot be empty!"})

    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        connection.close()

        if not result:
            return jsonify({"message": "Query executed successfully. No data returned."})

        return jsonify({"message": result})

    except Exception as e:
        return jsonify({"message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
