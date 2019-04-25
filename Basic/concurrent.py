import time
import asyncio

async def display_time():
    start_time = time.time()
    while True:
        dur = int(time.time() - start_time) 
        if dur % 3 == 0:
            print('{} seconds passed'.format(dur))
        await asyncio.sleep(1)

async def print_num():
    num =1
    while True:
        print(num)
        num+=1
        await asyncio.sleep(0.1)

"""
# for python 3.7
async def main():
    task1 = asyncio.create_task(display_time())
    task2 = asyncio.create_task(print_num())
    await asyncio.gather(task1,task2)

asyncio.run(main())
"""
# for below python 3.7

async def main():
    task1 = asyncio.ensure_future(display_time())
    task2 = asyncio.ensure_future(print_num())
    await asyncio.gather(task1,task2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()