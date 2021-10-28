from fastapi import FastAPI
from fileq import sum
from dif import diff 

app = FastAPI()


@app.get("/")
async def root():
    return sum(4,5)

@app.get("/diff")
async def root():
    return diff(4,5)