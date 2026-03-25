from fastapi import FastAPI
from apps.api.routes import recommend

app = FastAPI(title="Hybrid Recommender System")

app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Recommender API is running"}