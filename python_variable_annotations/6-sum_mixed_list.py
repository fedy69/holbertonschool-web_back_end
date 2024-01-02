#!/usr/bin/env python3
"""Annotaions list complex types"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of mixed list of float and int"""
    return sum(mxd_list)
