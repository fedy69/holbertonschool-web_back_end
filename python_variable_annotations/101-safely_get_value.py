#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """


from typing import TypeVar, Optional

T = TypeVar("T")


def safely_get_value(dct: dict[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
  """
  Returns the value associated with key in dct

  Args:
    dct: The dictionary to check.
    key: The key to look up.
    default: The value to return if key is not in dct.

  Returns:
    The value associated with key in dct
  """

  if key in dct:
    return dct[key]
  else:
    return default