"""
Mini Notes API - Tag 2: SQLite Version
"""



#Mini Notes API - Tag 3: SQLite Version

import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI-App erstellen
app = FastAPI(title="Mini Notes API", version="2.0.0")
# Datenbank-Dateiname
DATABASE = "notes.db"

def init_db():
"""Datenbank initialisieren und Tabelle erstellen."""
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
               
id INTEGER PRIMARY KEY AUTOINCREMENT,
text TEXT NOT NULL,
created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()               


# Beispiel-Daten (werden bei Neustart zurückgesetzt!)
notes = [
{"id": 1, "text": "Erste Notiz", "created_at": "2025-12-01T10:00:00"},
{"id": 2, "text": "Zweite Notiz", "created_at": "2025-12-01T14:30:00"},
]
@app.get("/health")
def health_check():
    """Health-Check Endpoint."""
    return {"status": "ok"}

@app.get("/notes")
def get_all_notes():
    """Gibt alle Notizen zurück."""
    return notes
