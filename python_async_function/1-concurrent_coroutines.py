#!/usr/bin/env python3
""" Async task 1 """


import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Async routine that spawns wait_random n times"""
    list_delays: List[float] = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_delays.append(delay)

    return sorted(list_delays)
