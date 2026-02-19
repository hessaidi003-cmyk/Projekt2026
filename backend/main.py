
#Mini Notes API - Tag 2: SQLite Version

import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI-App erstellen
app = FastAPI(title="Mini Notes API", version="2.0.0")
# Datenbank-Dateiname
DATABASE = "notes.db"





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
