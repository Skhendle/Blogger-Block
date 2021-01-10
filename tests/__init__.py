from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

# Configure a in memeory test database


client = TestClient(app)


