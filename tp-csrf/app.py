from flask import Flask, request
import subprocess
import hashlib

app = Flask(__name__)


ADMIN_PASSWORD = "123456"

def hash_password(password):
  
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if username == "admin" and hash_password(password) == hash_password(ADMIN_PASSWORD):
        return "Logged in"
    return "Invalid credentials"

@app.route("/ping")
def ping():
    host =
