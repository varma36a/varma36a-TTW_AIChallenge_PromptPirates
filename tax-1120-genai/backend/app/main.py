from fastapi import FastAPI
from app.routes.tax import tax_router as router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Tax 1120 GenAI API Running"}