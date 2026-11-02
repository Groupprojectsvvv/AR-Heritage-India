from pathlib import Path
import json
from flask import Flask, jsonify, send_from_directory

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
DATA = Path(__file__).resolve().parent / "data" / "monuments.json"
app = Flask(__name__, static_folder=str(FRONTEND), static_url_path="")

with DATA.open(encoding="utf-8") as stream:
    MONUMENTS = json.load(stream)

@app.get("/")
def home():
    return send_from_directory(FRONTEND, "index.html")

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "AR Heritage India"})

@app.get("/api/monuments")
def monuments():
    return jsonify([{"id": m["id"], "name": m["name"], "location": m["location"], "summary": m["summary"], "image": m["images"][0]["url"]} for m in MONUMENTS])

@app.get("/api/monuments/<slug>")
def monument(slug):
    item = next((m for m in MONUMENTS if m["id"] == slug), None)
    if item is None:
        return jsonify({"error": "Monument not found", "available": [m["id"] for m in MONUMENTS]}), 404
    return jsonify(item)

@app.get("/api/quiz/<slug>")
def quiz(slug):
    item = next((m for m in MONUMENTS if m["id"] == slug), None)
    if item is None:
        return jsonify({"error": "Monument not found"}), 404
    return jsonify(item["quiz"])

@app.get("/docs/<path:filename>")
def project_docs(filename):
    return send_from_directory(ROOT / "docs", filename)

@app.errorhandler(500)
def server_error(_error):
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == "__main__":
    # Bind to the local network so a phone on the same Wi-Fi can open the site.
    # Use only on a trusted private network; this is Flask's development server.
    app.run(host="0.0.0.0", port=5000, debug=False)
