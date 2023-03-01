from fastapi import FastAPI

app = FastAPI(
    title="Hello World",
    # root_path="/api",
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}