import asyncio

f = open("log.txt", "w+")
j = 0


async def worker1():
    global j
    for i in range(0, 2_000_000):
        j += 1
        print(f"A: {str(j).rjust(10, ' ')}", file=f)


async def workder2():
    global j
    for i in range(0, 2_000_000):
        j += 1
        print(f"B: {str(j).rjust(10, ' ')}", file=f)


async def main():
    task1 = asyncio.create_task(worker1())
    task2 = asyncio.create_task(workder2())
    await task1
    await task2


asyncio.run(main())
