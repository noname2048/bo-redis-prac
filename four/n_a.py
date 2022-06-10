import asyncio
import time


async def wash_clothes(basket):
    next_basket = []
    for clothes in basket:
        print(f"{time.strftime('%M:%S')} ... ▷wash {clothes}")
        await asyncio.sleep(3)
        print(f"{time.strftime('%M:%S')} ... ▶wash {clothes}")
        next_basket += [clothes]

    return next_basket


async def hang_clothes(basket):
    next_basket = []
    for clothes in basket:
        print(f"{time.strftime('%M:%S')} ... ▷hang clothes {clothes}")
        await asyncio.sleep(3)
        print(f"{time.strftime('%M:%S')} ... ▶hang clothes {clothes}")
        next_basket += [clothes]

    return next_basket


async def clean_myroom():
    print(f"{time.strftime('%M:%S')} ... ▷clean my room")
    await asyncio.sleep(20)
    print(f"{time.strftime('%M:%S')} ... ▶clean my room ")


async def main():
    basket = ["socks", "pants", "t-shirts", "towels"]
    wash_task = asyncio.create_task(wash_clothes(basket))
    clean_task = asyncio.create_task(clean_myroom())
    basket = await wash_task
    hang_task = asyncio.create_task(hang_clothes(basket))
    await clean_task
    await hang_task


asyncio.run(main())
