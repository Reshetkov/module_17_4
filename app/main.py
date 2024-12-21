from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)

app.include_router(task.router)

#  python -m uvicorn main:app
# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"
# cd app


# alembic upgrade head