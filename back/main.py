from fastapi import FastAPI, APIRouter
from routes.auth import router as auth_router
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from routes.event import router as event_router

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, prefix="/users", tags=["Authentications"])
app.include_router(event_router, prefix="/api", tags=["events"])