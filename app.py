from flask import Flask
import os

app = Flask(__name__)


@app.route("/home")
def home():
	return "Hello Sir Newton"


if __name__ == '__main__':
	app.run(debug = True, port = int(os.environ.get("PORT", 8080)))