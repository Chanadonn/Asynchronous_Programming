# example of runing a coroutine
import asyncio

# define a coroutine
async def custom_coro():
    # wait for a tal task to be done
    # await another coroutine
    await asyncio.sleep(1)

# main coroutine
async def main():
    # execute my custom coroutine
    await custom_coro()

# start the coroutine programs
asyncio.run(main())
