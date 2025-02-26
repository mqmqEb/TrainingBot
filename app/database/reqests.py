from app.database.training import async_session
from app.database.training import User
from sqlalchemy import select



async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_target(tg_id: int, target: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:            
            user.target = target
            await session.commit()

async def set_training_time(tg_id: int, time: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:            
            user.training_programme_time = time
            await session.commit()


async def set_start_time(tg_id: int, today: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:            
            user.start_time = today
            await session.commit()

async def set_end_time(tg_id: int, end: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:            
            user.end_time = end
            await session.commit()

async def set_lvl(tg_id: int, lvl: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:            
            user.lvl = lvl
            await session.commit()

async def get_info(tg_id: int):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))