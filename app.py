from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CloudNotes</h1>
    <p>My first Azure cloud application.</p>
    <p>Project 1: Real Cloud Web App</p>
    """

if __name__ == "__main__":
    app.run(debug=True)