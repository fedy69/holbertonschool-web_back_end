#!/usr/bin/env python3
""" Async task 0 """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronus coroutine waits for delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
