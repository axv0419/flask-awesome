from flask import Flask, render_template,request
import os

application = Flask(__name__)

OHIO = "/tmp/ohio.txt"
@application.route("/", methods=['GET', 'POST'])
def index():
    rval = "{}"
    if os.path.exists(OHIO):
        with open(OHIO,"r") as f:
            rval = f.read()
    request.on_json_loading_failed = lambda e: ({"error":f"Request data is not good JSON - {e}"})
    payload = request.get_json()
    with open(OHIO,"w") as f:
        f.write(f"{payload}")
    return rval

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)