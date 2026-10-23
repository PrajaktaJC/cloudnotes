from flask import Flask, request, redirect
from database import (
    get_notes,
    add_note,
    delete_note,
    get_note,
    update_note
)

app = Flask(__name__)


@app.route("/")
def home():
    notes = get_notes()

    html = """
    <h1>CloudNotes</h1>

    <form method="POST" action="/add">
        <p>Title</p>
        <input type="text" name="title" required>

        <p>Content</p>
        <textarea name="content" required></textarea>

        <br><br>

        <button type="submit">Add Note</button>
    </form>

    <hr>

    <h3>Notes stored in Azure SQL</h3>
    <ul>
    """

    for note in notes:
        html += f"""
        <li>
            <strong>{note.Title}</strong>: {note.Content}

            <form method="POST" action="/delete/{note.Id}">
                <button type="submit">Delete</button>
            </form>

            <form method="GET" action="/edit/{note.Id}">
                <button type="submit">Edit</button>
            </form>

        </li>
        """

    html += "</ul>"

    return html


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    content = request.form["content"]

    add_note(title, content)

    return redirect("/")


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    delete_note(note_id)

    return redirect("/")


@app.route("/edit/<int:note_id>")
def edit_page(note_id):

    note = get_note(note_id)

    return f"""
    <h1>Edit Note</h1>

    <form method="POST" action="/update/{note.Id}">

        <p>Title</p>
        <input
            type="text"
            name="title"
            value="{note.Title}"
            required>

        <p>Content</p>
        <textarea
            name="content"
            required>{note.Content}</textarea>

        <br><br>

        <button type="submit">
            Update Note
        </button>

    </form>

    <br>

    <a href="/">Back</a>
    """


@app.route("/update/<int:note_id>", methods=["POST"])
def update(note_id):

    title = request.form["title"]
    content = request.form["content"]

    update_note(
        note_id,
        title,
        content
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
