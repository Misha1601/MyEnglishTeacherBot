import asyncio

async def one():
    a = 0
    while a < 10:
        print("спим 2 секунды")
        await asyncio.sleep(2)
        a += 1

async def two():
    b = 0
    while b < 10:
        await asyncio.sleep(3)
        print("спим 3 секунды")
        b += 1

async def main():
    task1 = loop.create_task(one())
    task2 = loop.create_task(two())
    await asyncio.wait([task1, task2])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
