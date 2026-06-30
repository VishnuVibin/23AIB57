from flask import Flask, request, jsonify
from logging_middleware import Log
app = Flask(__name__)
@app.route("/login", methods=["POST"])
def login():
    Log("backend", "info", "login", "Login request received.")
    data = request.get_json()
    if not data:
        Log("backend", "warning", "validation", "Request body is empty.")
        return jsonify({"error": "No data provided"}), 400
    try:
        username = data.get("username")
        Log("backend", "info", "handler", f"Processing login for user '{username}'.")
        Log("backend", "info", "database", f"User '{username}' processed successfully.")
        return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        Log("backend", "fatal", "handler", f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500
if __name__ == "__main__":
    app.run(debug=True)