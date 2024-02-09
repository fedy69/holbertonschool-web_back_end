#!/usr/bin/env python3
""" Main file """


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count calls of method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """counter for count"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return counter


def call_history(method: Callable) -> Callable:
    """call history decorator"""

    @wraps(method)
    def history(self, *args, **kwargs):
        """append method to history"""
        inputkey = method.__qualname__ + ":inputs"
        outputkey = method.__qualname__ + ":outputs"
        output = method(self, *args, **kwargs)
        self._redis.rpush(inputkey, str(args))
        self._redis.rpush(outputkey, str(output))

        return output
    return history


def replay(method: Callable):
    """replay decorator"""
    self = method.__self__
    inputkey = method.__qualname__ + ":inputs"
    outputkey = method.__qualname__ + ":outputs"
    count = self.get_str(method.__qualname__)
    print(f"{method.__qualname__} was called {count} times:")
    inputs = self._redis.lrange(inputkey, 0, -1)
    outputs = self._redis.lrange(outputkey, 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            self.store.__qualname__,
            i[0].decode(),
            i[1].decode())
        )


class Cache():
    """Cache class"""
    def __init__(self) -> None:
        """ Initialize method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""

        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        """ Get method """
        data = self._redis.get(key)

        if fn:
            return fn(data)

        if fn is None:
            return data

    def get_str(self, key: str) -> str:
        """ Get method """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Get method """
        return self.get(key, int)
