from Krisztina_NagyVaci_work import anagramm
from Krisztina_NagyVaci_work import count_letters
import unittest

class Test(unittest.TestCase):
    def test_anagramm(self):
        self.assertTrue(anagramm('Alma', 'mala'))

    def test_anagram_numbers(self):
        self.assertTrue(anagramm('123', '321'))


    def test_count_letters(self):
        dict = {'l': 1, 'a': 2}
        self.assertEqual(count_letters('ala'), dict)
        self.assertEqual(count_letters('Ala'), dict)

if __name__ == '__main__':
    unittest.main()
