from fastapi import FastAPI

app = FastAPI(title="Simple API")

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}! (via FastAPI)"}
