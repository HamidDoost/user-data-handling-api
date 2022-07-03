from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_async_session, init_db
from app.models.user_model import User

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [
        User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            age=user.age,
            id=user.id,
        )
        for user in users
    ]


@router.post("/",status_code=201)
async def add_user(user: User, session: AsyncSession = Depends(get_async_session)):
    user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        age=user.age
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
