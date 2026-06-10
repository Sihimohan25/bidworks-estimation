from fastapi import FastAPI

app = FastAPI(
    title="BidWorks API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "BidWorks API Running"}