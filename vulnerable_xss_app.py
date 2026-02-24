
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

comments = []
VULNERABLE_MODE = True  # Toggle to enter safe mode

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form.get("user")
        text = request.form.get("comment")
        comments.append({"user": user, "text": text})

    resp = make_response(
        render_template(
            "index.html",
            comments=comments,
            vulnerable=VULNERABLE_MODE
        )
    )

    resp.set_cookie("sessionid", "USER-SESSION-999")
    return resp

if __name__ == "__main__":
    app.run(port=5000, debug=True)
