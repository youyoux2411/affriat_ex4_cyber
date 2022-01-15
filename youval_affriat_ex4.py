import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
async def sum_fun(a: int, b: int):
    response = "<html><body><h1>The result of " + str(a) + " + " + str(b) + " = " + str(a + b) + "</h1></body></html>"
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
