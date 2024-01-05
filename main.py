import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter

from db.config import settings
from api.pies.views import router as pies_router
from api.users.views import router as users_router
from demo.auth.views import router as demo_auth
from demo.auth.jwt_auth import router as demo_jwt_auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Now through alembic migrations
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="PyRog", lifespan=lifespan)

api_v1 = APIRouter(prefix=settings.api_v1_prefix)
api_v1.include_router(pies_router, prefix="/pies", tags=["Pies"])
api_v1.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(api_v1)

demo = APIRouter(prefix="/demo")
demo.include_router(demo_auth, prefix="/demo-auth", tags=["Demo Auth"])
demo.include_router(demo_jwt_auth, prefix="/emo_jwt_auth", tags=["Demo JWT Auth"])
app.include_router(demo)


@app.get("/")
def welcome_project():
    return {"message": "Welcome to project 'PyRog'"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
