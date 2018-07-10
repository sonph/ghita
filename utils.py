from typing import List, Any

def transpose(
    arrays: List[List[Any]], fill: Any = None) -> List[List[Any]]:
  """Transpose a list of lists, for table display in Vue.

  >>> transpose([['a', 'b'], [1, 2, 3]])
  [['a', 1], ['b', 2], [None, 3]]
  """
  # Can't use max(iterable) in transcrypt here.
  longestLength = len(arrays[0])
  for array in arrays:
    if len(array) > longestLength:
      longestLength = len(array)
  ret = []  # type: List[List[Any]]
  for i in range(longestLength):
    ret.append([])
    for array in arrays:
      value = array[i] if i < len(array) else fill
      ret[i].append(value)
  return ret


def rotate(array: List[Any], num: int) -> List[Any]:
  """Shifts elements to the left, cycling to the back, returning a new array.

  >>> rotate([1, 2, 3, 4, 5], 2)
  [3, 4, 5, 1, 2]
  """
  num = num % len(array)
  return array[num:].concat(array[0:num])
