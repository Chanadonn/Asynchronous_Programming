# example of an asynchronous iterator with async for loop
import asyncio
import time

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0
    
    # create an instance of the iterator
    def __aiter__(self):
        return self
    
    # return the next awitable
    async def __anext__(self):
        # check for no furture  items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter
# main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(f'{time.ctime()} {item}')
# execute the asycio program
asyncio.run(main())

#ANS
# Wed Jul 19 13:56:53 2023 1
# Wed Jul 19 13:56:54 2023 2
# Wed Jul 19 13:56:55 2023 3
# Wed Jul 19 13:56:56 2023 4
# Wed Jul 19 13:56:57 2023 5
# Wed Jul 19 13:56:58 2023 6
# Wed Jul 19 13:56:59 2023 7
# Wed Jul 19 13:57:00 2023 8
# Wed Jul 19 13:57:01 2023 9
# Wed Jul 19 13:57:02 2023 10