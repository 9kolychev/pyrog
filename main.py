from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from db import Base, DataBaseHelper, db_helper
from api.pies.views import router as pies_router
from api.users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="PyRog", lifespan=lifespan)
# create the instance for the routes
# main_api_router = APIRouter()
# set routes to the app instance
# main_api_router.include_router(users_router, prefix="/users", tags=["Users"])
# app.include_router(main_api_router)

app.include_router(pies_router, prefix="/pies", tags=["Pies"])
app.include_router(users_router, prefix="/users", tags=["Users"])


@app.get("/")
def welcome_project():
    return {"message": "Welcome to project 'PyRog'"}


if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
