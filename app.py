from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello World CONSOLE")
    return "Hello World RETURN"

if __name__ == "__main__":
    app.run()