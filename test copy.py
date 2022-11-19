import asyncio
import time

async def stroka():
    a = "hellow 5555"
    await asyncio.sleep(5)
    b = "hellow 6666"
    return a, b

async def stroka2():
    await asyncio.sleep(3)
    a = "hellow 3333"
    return a

async def main():
    b = await asyncio.gather(stroka(), stroka2())
    print(b)
    print(type(b))

t = time.time()
asyncio.run(main())
print(time.time()-t)