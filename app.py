from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CloudNotes</h1>
    <p>My first Azure cloud application.</p>
    <p>Hosted on Azure App Service</p>
    <p>Project 1: Real Cloud Web App</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0")
