import os
from flask import Flask, render_template, request, jsonify
from agent.core import SkillBridgeAgent
from tools.data_query import get_all_students, add_student_score, get_student_score

app = Flask(__name__)
agent = SkillBridgeAgent()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/students", methods=["GET"])
def list_students():
    try:
        students = get_all_students()
        return jsonify({"success": True, "students": students})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/students", methods=["POST"])
def create_or_update_student():
    data = request.get_json() or {}
    name = data.get("student_name", "").strip()
    track = data.get("track", "").strip()
    score = data.get("score")
    date = data.get("assessment_date", "").strip() or None

    if not name:
        return jsonify({"success": False, "error": "Student name is required."}), 400
    if not track:
        return jsonify({"success": False, "error": "Track is required."}), 400
    try:
        score = int(score)
    except (TypeError, ValueError):
        return jsonify({"success": False, "error": "Score must be a valid number."}), 400

    ok = add_student_score(name, track, score, date)
    if ok:
        return jsonify({"success": True, "message": f"Successfully updated score for {name}."})
    else:
        return jsonify({"success": False, "error": "Failed to update record in scores.csv."}), 500

@app.route("/api/generate-roadmap", methods=["POST"])
def generate_roadmap():
    data = request.get_json() or {}
    student_name = data.get("student_name", "").strip()
    track = data.get("track", "Education & Technology").strip()
    current_info = data.get("current_info", "").strip()
    goal = data.get("goal", "").strip()
    weeks = data.get("weeks", 8)
    hours_per_week = data.get("hours_per_week", 10)

    if not student_name:
        return jsonify({"success": False, "error": "Please provide a student name."}), 400
    if not current_info:
        return jsonify({"success": False, "error": "Please describe current knowledge or skills."}), 400
    if not goal:
        return jsonify({"success": False, "error": "Please enter a target career or learning goal."}), 400

    try:
        result = agent.generate_detailed_roadmap(
            track=track,
            student_name=student_name,
            current_info=current_info,
            goal=goal,
            weeks=weeks,
            hours_per_week=hours_per_week
        )
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Skill Bridge AI server starting on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
