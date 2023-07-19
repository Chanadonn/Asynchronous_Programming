# example of an asynchronous context manager via async eith
import asyncio
import time

import asyncio

# define an asynchronous context manager
class AsyncContextManager:
    # enter the async context manager
    async def __aenter__(self):
        # report a message
        print(f'{time.ctime()} >enterring the context manager')
        # block for a moment
        await asyncio.sleep(0.5)

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        # report a message
        print(f'{time.ctime()} >exiting the context manager')
        # block for a moment
        await asyncio.sleep(0.5)
    
# define a simple coroutine
async def custom_coroutine():
    # create and use the asynchronous contex manager
    async with AsyncContextManager() as manager:
        # report the result
        print(f'{time.ctime()} within the manager')

# start the asyncio program
asyncio.run(custom_coroutine())

#ANS
# Wed Jul 19 14:27:03 2023 >enterring the context manager
# Wed Jul 19 14:27:04 2023 within the manager
# Wed Jul 19 14:27:04 2023 >exiting the context manager