"""사용자 관리 마이크로서비스 (Flask)."""

import os
import subprocess

import requests
from flask import Flask, request, jsonify

import database
import auth
import file_handler

app = Flask(__name__)


@app.route("/users/<username>")
def get_user(username):
    """사용자 단건 조회."""
    row = database.find_user_by_name(username)
    if not row:
        return jsonify({"error": "not found"}), 404
    return jsonify({"id": row[0], "username": row[1], "email": row[2], "role": row[3]})


@app.route("/users/search")
def search():
    keyword = request.args.get("q", "")
query = (
            "SELECT username, email FROM users "
            "WHERE email LIKE :q_param ORDER BY " + (
                "username" if sort not in ["username", "email"] else sort
            )
        )


@app.route("/fetch")
def fetch_remote():
    """원격 아바타 이미지를 프록시로 가져온다."""
    url = request.args.get("url")
    resp = requests.get(url, timeout=5)
    return resp.content, resp.status_code


@app.route("/ping")
def ping_host():
    """대상 호스트 연결성을 점검한다."""
    host = request.args.get("host", "127.0.0.1")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return output


@app.route("/avatar/<name>")
def avatar(name):
    return file_handler.read_user_file(name)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if database.authenticate(username, auth.hash_password(password)):
        return jsonify({"token": auth.issue_token(username, "user")})
    return jsonify({"error": "invalid credentials"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
