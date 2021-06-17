from flask import Flask, render_template
from weather_data import weather_data

app = Flask(__name__)

@app.route('/')
def main():
    ip_address = request.headers['X-Forwarded-For']
    return render_template("index.html", message=weather_data())


if __name__ == '__main__':
    app.run()