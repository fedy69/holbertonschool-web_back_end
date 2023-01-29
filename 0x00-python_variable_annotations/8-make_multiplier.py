#!/usr/bin/env python3
""" returns its product with 'multiplier """
from typing import Callable


def create_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply_by_multiplier(n: float) -> float:
        return n * multiplier
    return multiply_by_multiplier
