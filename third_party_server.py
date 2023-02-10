from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    # time.sleep(5)
    return {"success": "hello world"}

if __name__ == '__main__':
    app.run(port=8000, debug=True)