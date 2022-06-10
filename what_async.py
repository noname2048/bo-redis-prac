import redis.asyncio as aioredis
import asyncio
import time


async def say_after(s="d"):
    print(f"({s}) started_at  {time.strftime('%X')}")
    await asyncio.sleep(3)
    print(f"({s}) finished_at {time.strftime('%X')}")


async def merge():
    t1 = asyncio.create_task(say_after("o"))
    t2 = asyncio.create_task(say_after("b"))
    print(f"travel start {time.strftime('%X')}")
    await asyncio.sleep(6)
    print(f"travel end {time.strftime('%X')}")
    await t1
    await t2


async def straight():
    await say_after("c")
    await say_after("r")


asyncio.run(merge())
