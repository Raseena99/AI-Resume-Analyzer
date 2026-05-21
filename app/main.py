from fastapi import FastAPI

from .database import engine
from .database import Base
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes using Python and AI techniques",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API Running"
    }
