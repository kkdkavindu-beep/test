from flask import Flask, jsonify, render_template, request

from solver import solve_from_scramble

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/solve")
def solve():
    payload = request.get_json(silent=True) or {}
    scramble = payload.get("scramble", "")

    try:
        result = solve_from_scramble(scramble)
        return jsonify({"ok": True, **result})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
