from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Learning App Running</h1>
    <p>ENV: {os.getenv('APP_ENV')}</p>
    <p>DB HOST: {os.getenv('DB_HOST')}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
