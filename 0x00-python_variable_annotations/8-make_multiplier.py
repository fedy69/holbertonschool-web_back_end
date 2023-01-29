#!/usr/bin/env python3
""" returns its product with 'multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply_by(n: float) -> float:
        return n * multiplier
    return multiply_by
