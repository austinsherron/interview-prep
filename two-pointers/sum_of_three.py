import unittest

from typing import List


def has_sum_of_three(values: List[int], target: int) -> bool:
    current = 0
    low = 1
    high = len(values)



    if high < 3:
        return False

    total = target
    in_order = sorted(values)

    for i in values:
        

    return False


class TestSumOfThree(unittest.TestCase):
    pass


if __name__ == '__main__':

    unittest.main()

