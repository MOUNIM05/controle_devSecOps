from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
   
    return subprocess.check_output(cmd, shell=True)

if __name__ == "__main__":

    app.run(debug=True)
