import os
from sqlalchemy import create_engine, text

server = "sql-cloudnotes-praju.database.windows.net"
database = "cloudnotesdb"
username = "sqladmin"
password = os.getenv("DB_PASSWORD")

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:1433/"
    f"{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)

with engine.connect() as conn:
    result = conn.execute(text("SELECT TOP 1 * FROM Notes"))

    for row in result:
        print(row)

print("Database connection successful!")
