import unittest

# Reverses the given string.
def reverse_string(input_string):
    return input_string[::-1]

class TestReverseStringFunction(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
        self.assertEqual(reverse_string("racecar"), "racecar")

if __name__ == '__main__':
    unittest.main()
