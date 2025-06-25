from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import cat, mission
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cat.router)
app.include_router(mission.router)
