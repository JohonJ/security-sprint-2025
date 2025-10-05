from flask import Flask, request, render_template
from markupsafe import escape
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Security Sprint App!"

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    user_input = request.args.get('input')
    return render_template("response.html", user_input=user_input)

@app.route('/echo')
def echo():
    msg = request.args.get('msg', '')
    return f"You said: {msg}"

if __name__ == '__main__':  
    import os
    app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True")



