import unittest
import index

class TestIndex(unittest.TestCase):
    def test_reverseExists(self):
        self.assertTrue(hasattr(index, 'reverse') and callable(getattr(index, 'reverse')))
    def test_1(self):
        self.assertEqual(index.reverse("abcd"), "dcba")
    def test_2(self):
        self.assertEqual(index.reverse("  abcd"), "dcba  ")

if __name__ == '__main__':
    unittest.main()