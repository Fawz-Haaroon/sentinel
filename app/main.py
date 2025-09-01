from fastapi import FastAPI

from app.routers.health import router as health_router

app = FastAPI(title="CyberSentinel", version="0.1.0")

app.include_router(health_router)

@app.get("/")
def root():
    return {"status": "ok"}

