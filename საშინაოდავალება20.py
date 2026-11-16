import asyncio
import time


async def deliver(order, seconds):
    print(f"{order}: გაიგზავნა")
    await asyncio.sleep(seconds)
    print(f"{order}: მიტანილია")


async def main1():
    orders = [("შეკვეთა #1", 1.0), ("შეკვეთა #2", 1.5), ("შეკვეთა #3", 2.0)]

    start = time.perf_counter()
    for order, seconds in orders:
        await deliver(order, seconds)
    sequential = time.perf_counter() - start
    print(f"ზედიზედ: {sequential:.1f} წმ")

    start = time.perf_counter()
    await asyncio.gather(*(deliver(order, seconds) for order, seconds in orders))
    concurrent = time.perf_counter() - start
    print(f"ერთდროულად: {concurrent:.1f} წმ")

    print(f"დაჩქარება: {sequential / concurrent:.1f}x")


asyncio.run(main1())


async def square(number):
    await asyncio.sleep(1)
    return number * number


async def main2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    start = time.perf_counter()
    squares = await asyncio.gather(*(square(number) for number in numbers))
    elapsed = time.perf_counter() - start

    for number, result in zip(numbers, squares):
        print(f"{number}² = {result}")
    print("ჯამი:", sum(squares))
    print(f"დრო: {elapsed:.1f} წმ")


asyncio.run(main2())


async def load_user(user_id):
    await asyncio.sleep(1)
    return {"id": user_id, "name": f"მომხმარებელი {user_id}"}


async def main3():
    start = time.perf_counter()

    users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
    print(users)
    print(f"დრო: {time.perf_counter() - start:.1f} წმ")


asyncio.run(main3())