import unittest
import calc

class TestEmptyStringReturnsZero(unittest.TestCase):
    def test_empty_string_returns_0(self):
        expected = 0
        actual = calc.string("")
        self.assertEqual(expected, actual)
