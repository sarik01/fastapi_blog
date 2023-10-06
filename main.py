
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers
from redis import asyncio as aioredis
from fastapi import FastAPI, Request, Depends
from starlette.middleware.cors import CORSMiddleware

from src.auth.models import User
from src.auth.base_config import auth_backend

from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.operations.router import router
from src.tasks.router import celery_router

app = FastAPI(
    title="Blog App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router)
app.include_router(celery_router)

# For Frontend app
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://redis:6379", encoding='utf-8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')



