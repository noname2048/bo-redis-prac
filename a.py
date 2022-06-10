import redis
import redis.asyncio as aioredis
import asyncio
import async_timeout

STOPWORD = "STOP"


async def reader(channel: redis.client.PubSub):
    while True:
        try:
            async with async_timeout.timeout(1):
                message = await channel.get_message(ignore_subcribe_message=True)
                if message is not None:
                    print(f"(Reader) Message Received: {message}")
                    if message["data"].decode() == STOPWORD:
                        print("(Reader) STOP")
                        break
                await asyncio.sleep(0.01)
        except asyncio.TimeoutError:
            pass


async def main():
    r = aioredis.Redis(host="localhost", port=6379)
    ps = r.pubsub()
    await ps.subscribe("23")
    while True:
        message = await ps.get_message(ignore_subscribe_messages=True)
        print(message)


asyncio.run(main())
