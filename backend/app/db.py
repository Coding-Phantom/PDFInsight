# SQLite database to manage pdf records (seperate from embeddings/vectors)
# Vectors are stored in Chroma, not this database

import sqlite3
from pathlib import Path

# Initialize db connection
def get_connection(db_path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database(db_path: Path) -> None:
    db_path.parent.mkdir(exist_ok=True) # make sure parent directory exists

    with get_connection(db_path) as connection: # connect to database
        connection.execute( # create table of id, filename, file path, time/day created
            """
            CREATE TABLE IF NOT EXISTS pdfs (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

# add new pdf records into db, return as dict to confirm result
def create_pdf_record(db_path: Path, pdf_id: str, filename: str, file_path: Path) -> dict[str, str]:
    with get_connection(db_path) as connection:
        connection.execute(
            """
            INSERT INTO pdfs (id, filename, file_path)
            VALUES (?, ?, ?)
            """,
            (pdf_id, filename, str(file_path)),
        )

    pdf = get_pdf_record(db_path, pdf_id)
    if pdf is None:
        raise RuntimeError("PDF record was not created")

    return pdf

# list pdf records in pdf, return as dict to confirm result
def list_pdf_records(db_path: Path) -> list[dict[str, str]]:
    with get_connection(db_path) as connection:
        rows = connection.execute(
            """
            SELECT id, filename, file_path, created_at
            FROM pdfs
            ORDER BY created_at DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]

# retrieve pdf record from id, return as dict to confirm result
def get_pdf_record(db_path: Path, pdf_id: str) -> dict[str, str] | None:
    with get_connection(db_path) as connection:
        row = connection.execute(
            """
            SELECT id, filename, file_path, created_at
            FROM pdfs
            WHERE id = ?
            """,
            (pdf_id,),
        ).fetchone()

    return dict(row) if row else None

# delete pdf record from id, return deleted pdf
def delete_pdf_record(db_path: Path, pdf_id: str) -> dict[str, str] | None:
    pdf = get_pdf_record(db_path, pdf_id)
    if pdf is None:
        return None

    with get_connection(db_path) as connection:
        connection.execute("DELETE FROM pdfs WHERE id = ?", (pdf_id,))

    return pdf
