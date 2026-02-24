from flask import Flask, request, redirect

app = Flask(__name__)

balance = 25000
transactions = []

# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/dashboard")

    return """
<!DOCTYPE html>
<html>
<head>
<title>Secure Bank Login</title>
<style>
body{
    background:#0f172a;
    font-family:Arial;
    color:white;
}
.container{
    width:350px;
    margin:120px auto;
    background:#1e293b;
    padding:30px;
    border-radius:10px;
    box-shadow:0 0 10px black;
}
input,button{
    width:100%;
    padding:10px;
    margin-top:10px;
    border-radius:5px;
    border:none;
}
button{
    background:#2563eb;
    color:white;
    font-size:16px;
}
button:hover{
    background:#1d4ed8;
}
h2{text-align:center;}
</style>
</head>

<body>
<div class="container">
<h2>🔐 Secure Bank Login</h2>
<form method="POST">
<input placeholder="Username" required>
<input type="password" placeholder="Password" required>
<button>Login</button>
</form>
</div>
</body>
</html>
"""

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    history = "".join([f"<li>{t}</li>" for t in transactions])

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
<style>
body{{background:#0f172a;font-family:Arial;color:white;}}
.card{{
    width:600px;
    margin:30px auto;
    background:#1e293b;
    padding:25px;
    border-radius:10px;
}}
input,button{{
    padding:10px;
    margin-top:10px;
}}
button{{
    background:#16a34a;
    color:white;
    border:none;
    border-radius:5px;
}}
button:hover{{
    background:#15803d;
}}
h2,h3{{text-align:center;}}
</style>

</head>

<body>

<div class="card">
<h2>Welcome, User</h2>
<h3>Balance: ₹{balance}</h3>

<h3>Transfer Money</h3>
<form action="/transfer" method="POST">
<input type="number" name="amount" placeholder="Amount" required>
<br>
<button>Transfer</button>
</form>

<h3>Transaction History</h3>
<ul>{history}</ul>
</div>

</body>
</html>
"""

# ---------------- TRANSFER ENDPOINT (CSRF VULNERABLE) ----------------
@app.route("/transfer", methods=["POST"])
def transfer():
    global balance
    import time

    amt = request.form.get("amount")

    # Prevent crash
    if not amt:
        return redirect("/dashboard")

    amount = int(amt)

    if amount <= 0:
        return redirect("/dashboard")
    time.sleep(2)

    if amount > balance:
        transactions.append("❌ Transfer Failed (Insufficient Balance)")
    else:
        balance -= amount
        transactions.append(f"✅ Transferred ₹{amount}")

    return redirect("/dashboard")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)
