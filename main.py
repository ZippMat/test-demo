from fastapi import FastAPI, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select
from database import SessionLocal
import model
import schema


app = FastAPI()


async def get_db():
    async with SessionLocal() as session:
        yield session


@app.get("/")
async def root():
    return {"message": "Hello World V6"}


@app.get("/health")
async def health():
    return {"message": "Everything is good here"}


@app.get("/users", response_model=list[schema.UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(model.User))
    users = result.scalars().all()
    return users
