import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client["interns_b2_23"]
collection_users = db["SRIJAN"]


class User(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(username: str, password: str):
    if collection_users.find_one({"username": username}):
        return {"message": "cannot signup multiple times with same user"}
    user = collection_users.insert_one({"username": username, "password": password})
    if user:
        return {"message": "Signup successful"}
    else:
        raise HTTPException(status_code=444, detail="error")


@app.post("/login")
def login(username: str, password: str):
    usernames_data = collection_users.find_one({"username": username})
    if usernames_data["password"] == password:
        return {"message": "Login Successful"}
    else:
        return {"message": "Login failed"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=4000)
