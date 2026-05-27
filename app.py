from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Flask CI/CD Microservice Running"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    task = {
        "id": data["id"],
        "title": data["title"],
        "status": data["status"]
    }

    tasks.append(task)

    return jsonify(task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)