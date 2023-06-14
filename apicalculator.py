import uvicorn
from fastapi import FastAPI
app = FastAPI()


@app.get("/add")
def add_numbers(num1: float, num2: float):
    return{"result": num1 + num2}


@app.get("/subtract")
def subtract_numbers(num1: float, num2: float):
    return{"result": num1 - num2}


@app.get("/multiply")
def multiply_numbers(num1: float, num2: float):
    return{"result": num1 * num2}


@app.get("/divide")
def divide_numbers(num1: float, num2: float):
    if num2 == 0:
        return{"error": "cannot divide by zero"}
    return{"result": num1 / num2}


if __name__ == "__main__":
    uvicorn.run("main:app")