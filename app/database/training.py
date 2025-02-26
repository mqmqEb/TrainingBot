from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    tg_id = mapped_column(BigInteger, primary_key=True)
    target: Mapped[str] = mapped_column(String(25))
    training_programme_time: Mapped[int] = mapped_column()
    lvl: Mapped[int] = mapped_column()
    now_time: Mapped[int] = mapped_column()
    start_time: Mapped[str] = mapped_column(String(10))
    end_time: Mapped[str] = mapped_column(String(10))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)