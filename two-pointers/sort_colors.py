import unittest

from typing import List


def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def sort_colors(colors: List[int]) -> List[int]:
    low = 0
    high = 1

    current = 0
    end = len(colors)

    while low < end - 1:
        while high < end:
            if colors[low] == current:
                low += 1
            elif colors[high] == current:
                swap(colors, low, high)
                low += 1

            high += 1

        high = low + 1
        current += 1


    return colors


class TestSortColors(unittest.TestCase):

    def test_happy_path(self):
        print(sort_colors([0, 1, 0]))
        print(sort_colors([1, 1, 0, 2]))
        print(sort_colors([2, 1, 1, 0, 0]))
        print(sort_colors([2, 2, 2, 0, 1, 0]))
        print(sort_colors([2, 1, 1, 0, 1, 0, 2]))
        print(sort_colors([1, 0, 2, 1, 2, 2]))

    def test_edge_cases(self):
        print(sort_colors([]))
        print(sort_colors([0]))


if __name__ == '__main__':
    unittest.main()

