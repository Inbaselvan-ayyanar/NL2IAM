from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import main

app = Flask(__name__)
CORS(app)

# ✅ Global storage directory (change this once, applies everywhere)
STORAGE_DIR = r"C:/Users/ainba/Downloads/aws frontend/my-react-vite-app/backend"

# Make sure directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)


@app.route("/Group", methods=["POST"])
def group():
    file = request.files.get('file')
    if file:
        file_path = os.path.join(STORAGE_DIR, "data.csv")
        file.save(file_path)
        main.create_aws_Group()
        return jsonify({"status": "success", "saved_to": file_path})
    return jsonify({"status": False, "error": "No file received"})


@app.route("/download/group_report.csv", methods=["GET"])
def download_group_report():
    file_path = os.path.join(STORAGE_DIR, "group_report.csv")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "Report not found"}), 404


@app.route("/User", methods=["POST"])
def User():
    file = request.files.get("file")
    if file:
        file_path = os.path.join(STORAGE_DIR, "user_data.csv")
        file.save(file_path)
        main.create_aws_user()
        return jsonify({"status": "success", "saved_to": file_path})
    return jsonify({"status": False, "error": "No file received"})


@app.route("/download/user_report.csv", methods=["GET"])
def download_user_report():
    file_path = os.path.join(STORAGE_DIR, "user_report.csv")
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    print(1)
    return jsonify({"error": "Report not found"}), 404


@app.route("/")
def main1():
    return "<h1> hello </h1>"


if __name__ == '__main__':
    app.run(debug=True)
