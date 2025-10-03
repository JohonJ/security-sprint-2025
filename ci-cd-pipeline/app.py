from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Security Sprint App!"

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    user_input = request.args.get('input')
    return f"You entered: {user_input}"  # ⚠️ Vulnerable to XSS

if __name__ == '__main__':  
    import os
    app.run(debug=os.getenv("FLASK_DEBUG", "False") == "True")

