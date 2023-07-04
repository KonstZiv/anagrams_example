import unittest
from anagrams import tricky_invert_sentence


class TestAnagram(unittest.TestCase):
    typical_cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

    atypical_cases = [
        100,
        True,
        None,
        print,
    ]

    def test_typical(self):
        """
        Tests for typical cases.
        """
        for arg, result in self.typical_cases:
            with self.subTest(arg=arg, result=result):
                self.assertEqual(tricky_invert_sentence(arg), result)

    def test_atypical(self):
        """
        Test for atypical cases (wrong argument type).
        """
        for arg in self.atypical_cases:
            with self.assertRaises(TypeError):
                tricky_invert_sentence(arg)


if __name__ == "__main__":
    unittest.main()
