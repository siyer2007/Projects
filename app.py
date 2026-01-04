# app.py
from flask import Flask, request, jsonify
from exam_planner import generate_plan

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    subject = data.get("subject")
    days = int(data.get("days"))
    hours = int(data.get("hours"))

    plan = generate_plan(subject, days, hours)
    return jsonify(plan)

if __name__ == "__main__":
    app.run(debug=True)
