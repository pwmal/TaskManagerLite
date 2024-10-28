from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_table, delete_table
from router import router as router_tasks

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    await create_table()
    print("БД готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(router_tasks)
