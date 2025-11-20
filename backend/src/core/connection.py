# from functools import wraps

# from ..app.db import async_session_marker


# def connection(method):
#     @wraps(method)
#     async def wrapper(*args, **kwargs):
#         async with async_session_marker() as session:
#             try:
#                 return await method(*args, **kwargs, session=session)
#             except Exception as e:
#                 await session.rollback()
#                 raise e
#             finally:
#                 await session.close()

#     return wrapper
