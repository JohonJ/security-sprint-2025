from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Security Sprint App!"

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    user_input = request.args.get('input')
    safe_input = escape(user_input)
    return f"You entered: {safe_input}"

if __name__ == '__main__':
    app.run(debug=True)

