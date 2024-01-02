#!/usr/bin/env python3
""" Annotations - first element of a sequence """

from typing import Any, List, Optional

def safe_first_element(lst: List[Any]) -> Optional[Any]:
  """
  Returns the first element of a list, or None if the list is empty.

  Args:
    lst: The list to check.

  Returns:
    The first element of the list, or None if the list is empty.
  """

  if lst:
    return lst[0]
  else:
    return None
