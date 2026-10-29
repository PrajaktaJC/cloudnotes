import os
from sqlalchemy import create_engine, text

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_URL = "https://kv-cloudnotes-praju.vault.azure.net/"

password = os.getenv("DB_PASSWORD")

if not password:
    credential = DefaultAzureCredential()

    client = SecretClient(
        vault_url=KEY_VAULT_URL,
        credential=credential
    )

    password = client.get_secret("db-password").value

    print("DEBUG DB_PASSWORD =", password)

engine = None

def get_notes():
    if engine is None:
        return []

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT Id, Title, Content, CreatedAt FROM Notes")
        )
        return result.fetchall()


def add_note(title, content):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Notes (Title, Content)
                VALUES (:title, :content)
            """),
            {"title": title, "content": content}
        )
        conn.commit()


def delete_note(note_id):
    with engine.connect() as conn:
        conn.execute(
            text("""
                DELETE FROM Notes
                WHERE Id = :id
            """),
            {"id": note_id}
        )
        conn.commit()


def get_note(note_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT Id, Title, Content
                FROM Notes
                WHERE Id = :id
            """),
            {"id": note_id}
        )
        return result.fetchone()


def update_note(note_id, title, content):
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE Notes
                SET Title = :title,
                    Content = :content
                WHERE Id = :id
            """),
            {
                "id": note_id,
                "title": title,
                "content": content
            }
        )
        conn.commit()
