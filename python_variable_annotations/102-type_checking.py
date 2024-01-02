#!/usr/bin/env python3
""" Complex types - functions """

from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
  """
  Returns a new list that is a zoom-in of the original list.

  Args:
    lst: The list to zoom in on.
    factor: The zoom factor.

  Returns:
    A new list that is a zoom-in of the original list.
  """

  zoomed_in: List[int] = []
  for item in lst:
    for i in range(factor):
      zoomed_in.append(item)

  return tuple(zoomed_in)


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
