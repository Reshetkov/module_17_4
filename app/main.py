from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)

app.include_router(task.router)

# cd app
#  python -m uvicorn main:app   (потом это)
# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"



# alembic upgrade head    (Сначала это)