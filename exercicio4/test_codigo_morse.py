from unittest import TestCase
from codigo_morse import possibilities
TestCase.maxDiff = None

class TestSampleTestCases(TestCase):
    def test_works_on_a_single_signal(self):
        "works on a single signal"
        self.assertEqual(possibilities("."), ["E"])
        self.assertEqual(possibilities(".-"), ["A"])

    def test_works_on_a_word_with_a_single_unknown_signal(self):
        "works on a word with a single unknown signal"
        self.assertEqual(possibilities("?"), ["E", "T"])
        self.assertEqual(possibilities("?."), ["I", "N"])
        self.assertEqual(possibilities(".?"), ["I", "A"])
