import unittest
from translator import english_to_french
from translator import french_to_english

class TestMachineTranslation(unittest.TestCase):

    def english_to_french(self):
        self.assertEqual(english_to_french(''), '') # If the input is "Null" the output is "Null"
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # If the input is "Hello" the output is "Bonjour"

    def french_to_english(self):
        self.assertEqual(french_to_english(''), '') # If the input is "Null" the output is "Null"
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # If the input is "Bonjour" the output is "Hello"

if __name__ == '__main__':
    unittest.main()