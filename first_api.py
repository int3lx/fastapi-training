from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="My first API",
    description="API to just to say hello.",
    version="0.1.0",
)

@app.get("/hello", tags=["Greeting"])
def hello_fastapi():
    return {"message": "Hello, FastAPI!"}
