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
