import unittest


def is_palindrome(string: str) -> bool:
    if string == "":
        return False

    start, end = 0, len(string) - 1
    while start <= end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True


class TestPalindrome(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(is_palindrome(""))

    def test_palindromes(self):
        self.assertTrue(is_palindrome("anna"))
        self.assertTrue(is_palindrome("civic"))
        self.assertTrue(is_palindrome("wow wow"))
        self.assertTrue(is_palindrome("amanaplanacanalpanama"))

    def test_not_palindromes(self):
        self.assertFalse(is_palindrome("word"))
        self.assertFalse(is_palindrome("ordinary"))
        self.assertFalse(is_palindrome("planner"))
        self.assertFalse(is_palindrome("planar"))


if __name__ == '__main__':

    unittest.main()

