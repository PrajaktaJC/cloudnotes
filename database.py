import os
from sqlalchemy import create_engine, text

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_URL = "https://kv-cloudnotes-praju.vault.azure.net/"

credential = DefaultAzureCredential()
client = SecretClient(
    vault_url=KEY_VAULT_URL,
    credential=credential
)

password = client.get_secret("db-password").value

server = "sql-cloudnotes-praju.database.windows.net"
database = "cloudnotesdb"
username = "sqladmin"

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:1433/"
    f"{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)


def get_notes():
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
