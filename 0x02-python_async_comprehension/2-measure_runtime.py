#!/usr/bin/env python3

""" this is a method """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ this is a method """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
