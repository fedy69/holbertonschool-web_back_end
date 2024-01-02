#!/usr/bin/env python3
""" Tasks """


from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Async routine that spawns wait_random n times"""
    list_delays: List[float] = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        list_delays.append(delay)

    return sorted(list_delays)
