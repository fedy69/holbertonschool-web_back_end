#!/usr/bin/env python3
"""Async parallel comprehension"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension 4 times"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.perf_counter() - start
    return end
