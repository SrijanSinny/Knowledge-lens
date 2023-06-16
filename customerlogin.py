from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI, Request

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
collection = db.Srijan_766


class customer(BaseModel):
    username: str
    password: str
    email: str
    phone_no: str

# customer details inserting here
@app.post("/customer_signup")
async def customer_signup(request: Request):
    data = await request.form()
    Customer = customer(
        username=data["username"],
        password=data["password"],
        email=data["email"],
        phone_no=data["phone_no"],
    )
    collection.insert_one(Customer.dict())
    return {"message": "Sign up page created successfully"}

# fetching customer details here
@app.post("/customer_login")
async def customer_login(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"]
    Customer = collection.find_one({"username": username, "password": password})
    if Customer:
        return {"message": "login  Successfull"}
    else:
        return {"error": "Login failed,username or password is wrong!!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5001)
