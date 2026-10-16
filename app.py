from flask import Flask
from database import get_notes

app = Flask(__name__)


@app.route("/")
def home():
    notes = get_notes()

    html = """
    <h1>CloudNotes</h1>
    <h3>Notes stored in Azure SQL</h3>
    <ul>
    """

    for note in notes:
        html += f"<li><strong>{note.Title}</strong>: {note.Content}</li>"

    html += "</ul>"

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0")
