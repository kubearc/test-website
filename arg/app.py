from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {os.getenv('APP_NAME', 'MyApp')} v{os.getenv('APP_VERSION', '1.0.0')}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", 8080)))
