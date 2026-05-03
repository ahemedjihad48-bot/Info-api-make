# main.py
# Free Fire OB53 Info API (API Only)
# Run: pip install flask
# Start: python main.py

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Demo Database
# -----------------------------
OB53_DATA = {
    "version": "OB53",
    "game": "Free Fire",
    "status": "upcoming",
    "release_date": "2026-06-20",
    "features": [
        {
            "type": "character",
            "name": "New Hero",
            "skill": "Speed Boost"
        },
        {
            "type": "weapon",
            "name": "M1887 Evo",
            "buff": "+Damage"
        },
        {
            "type": "map",
            "name": "Bermuda",
            "change": "New Area Added"
        },
        {
            "type": "event",
            "name": "OB53 Launch Event",
            "reward": "Free Bundle"
        }
    ]
}

PLAYERS = {
    "10609031393": {
        "uid": "10609031393",
        "name": "JIHAD X",
        "level": 72,
        "rank": "Heroic",
        "region": "BD"
    },
    "123456789": {
        "uid": "123456789",
        "name": "PLAYER X",
        "level": 55,
        "rank": "Diamond",
        "region": "IND"
    }
}

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "name": "Free Fire OB53 API",
        "status": "online",
        "time": str(datetime.utcnow()),
        "endpoints": [
            "/api/ob53",
            "/api/features",
            "/api/player/<uid>",
            "/api/search?name=player"
        ]
    })

# -----------------------------
# OB53 Info
# -----------------------------
@app.route("/api/ob53")
def ob53():
    return jsonify(OB53_DATA)

# -----------------------------
# Features Only
# -----------------------------
@app.route("/api/features")
def features():
    return jsonify({
        "version": "OB53",
        "count": len(OB53_DATA["features"]),
        "data": OB53_DATA["features"]
    })

# -----------------------------
# Player Lookup
# -----------------------------
@app.route("/api/player/<uid>")
def player(uid):
    if uid in PLAYERS:
        return jsonify({
            "success": True,
            "data": PLAYERS[uid]
        })
    return jsonify({
        "success": False,
        "message": "Player not found"
    }), 404

# -----------------------------
# Search by Name
# -----------------------------
@app.route("/api/search")
def search():
    name = request.args.get("name", "").lower()

    result = []
    for uid, data in PLAYERS.items():
        if name in data["name"].lower():
            result.append(data)

    return jsonify({
        "success": True,
        "count": len(result),
        "results": result
    })

# -----------------------------
# Start Server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)