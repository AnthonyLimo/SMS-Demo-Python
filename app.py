import os
from flask import Flask, request, render_template
import africastalking

app = Flask(__name__)

username = "sandbox"
api_key = "e7d4234186242a654f3beaf858a5f87da565ebb6a4486e14a2b19e4b799bd4cc"

africastalking.initialize(username, api_key)

sms = africastalking.SMS

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        phone_number = request.form["phoneNumber"]
        message = request.form["message"]

        try:
            response = sms.send(message, [phone_number])
            print(response)
            return render_template("success.html")
        except Exception as e:
            print(f"Houston, we have a problem {e}")
            return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, port = os.environ.get("PORT"))

