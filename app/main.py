from fastapi import FastAPI
from app.firebase import db

app = FastAPI()


@app.get("/")
def home():
    return {"message": "E-Waris Backend Running Successfully"}


# Generic function (reuse logic)
def fetch_collection(collection_name: str):
    docs = db.collection(collection_name).stream()

    results = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        results.append(data)

    return results


@app.get("/users")
def get_users():
    return fetch_collection("Users")


@app.get("/assets")
def get_assets():
    return fetch_collection("Assets")


@app.get("/nominees")
def get_nominees():
    return fetch_collection("Nominees")
