from flask import Flask, jsonify
from utility import get_request, check_interval

app = Flask(__name__)

@app.route('/')
def home():
    response = get_request()
    # print(response.text)
    return response.text

if __name__ == '__main__':
    check_interval()
    app.run(debug=True)