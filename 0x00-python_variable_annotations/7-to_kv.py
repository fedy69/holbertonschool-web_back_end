#!/usr/bin/env python3
""" String and int/float to tuple """
from typing import Tuple, Union
<<<<<<< HEAD
=======


>>>>>>> 9743c857917fc0ccb8b3188e186fc5e853c1f56a


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
