import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import current_active_user
from src.auth.models import User, post
from src.database import get_async_session

from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix='/posts',
    tags=["Posts"]
)


@router.get('/{item_id}')
async def get_post(item_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(post).where(post.c.id == item_id)
        result = await session.execute(query)

        return result.mappings().first()
    except Exception as e:
        print(e)
        return {'status': 'not found!'}

@router.get('/')
@cache(expire=30)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    query = select(post)
    time.sleep(2)
    result = await session.execute(query)
    return result.mappings().all()


@router.put('/{item_id}')
async def upd_post(new_post: OperationCreate, item_id: int,
                   session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    try:
        post_item = await session.execute(select(post).where(post.c.id == item_id))

        post_user_id = post_item.mappings().first()['user_id']

        if user.id == post_user_id:
            upd = update(post).where(post.c.id == item_id).values(**new_post.dict())

            await session.execute(upd)
            await session.commit()

            return {'status': 'success'}
        return {'status', 'bad'}
    except Exception as e:
        print(e)
        return {'status': 'bad'}, 400


@router.post('/')
async def add_post(new_post: OperationCreate, session: AsyncSession = Depends(get_async_session),
                   user: User = Depends(current_active_user)):
    try:
        stmt = insert(post).values(**new_post.dict())
        await session.execute(stmt)
        await session.commit()

        return {'status': 'success'}
    except Exception as e:
        print(e)
        {'status': 'bad'}, 400


@router.delete('/{item_id}')
async def delete_item(item_id: int, session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_active_user)):
    try:
        post_item = await session.execute(select(post).where(post.c.id == item_id))

        post_user_id = post_item.mappings().first()['user_id']

        if user.id == post_user_id:

            stmt = delete(post).where(post.c.id == item_id)

            await session.execute(stmt)
            await session.commit()

            return {'status': 'success'}
        else:
            return {'status': 'bad'}, 400

    except Exception as e:
        print(e)
        return {'status': 'bad'}, 400


