import redis.asyncio as redis
from redis.client import PubSub
import asyncio
import async_timeout
import time

STOPWORD = "STOP"


async def reader(channel: PubSub):
    while True:
        try:
            async with async_timeout.timeout(30):
                message = await channel.get_message()
                if message is None:
                    pass
                else:
                    print(f"{time.strftime('%X')}: {message}")
                    if (
                        type(message["data"]) == str
                        and message["data"].decode() == STOPWORD
                    ):
                        print("STOP")
                        break
                await asyncio.sleep(0.2)
        except asyncio.TimeoutError:
            break


async def main():
    r = await redis.from_url("redis://localhost")
    pubsub = r.pubsub()
    await pubsub.psubscribe("channel:*")
    future = asyncio.create_task(reader(pubsub))

    await future


if __name__ == "__main__":
    asyncio.run(main())
