# example of gettine the task from the main coroutine
import asyncio
import time

# define a main coroutine
async def main():
    # report a message
    print(f'{time.ctime()}main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(f'{time.ctime()}{task}')

#start the asyncio program
asyncio.run(main())

#ANS
# Wed Jul 12 14:22:17 2023main coroutine started
# Wed Jul 12 14:22:17 2023<Task pending name='Task-1' coro=<main() running at F:\Kith\Work\วิชาการพัฒนาระบบอะซิโครนัส\2-asyncio.py:12> cb=[_run_until_complet
# e_cb() at C:\Users\Kith\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py:180]>