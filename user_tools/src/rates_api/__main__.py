
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() -> str:
    """ home """
    return "Hello, World!"


def start_rates_api() -> None:
    """ start rates api """

    app.run()

if __name__ == "__main__":
    start_rates_api()
