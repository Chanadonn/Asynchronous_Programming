# example of gather for many coroutines in a list
import asyncio
import time

# coroutine use for a tak
async def task_coro(value):
    # report a message
    print(f'{time.ctime()} task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point
async def main():
    # report a message
    print(f'{time.ctime()} main starting.')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print(f'{time.ctime()} main done')

# start the asyncio program
asyncio.run(main())