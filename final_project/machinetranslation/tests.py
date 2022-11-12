import unittest
class TestTranslator(unittest.TestCase):

    def english_to_french(self):
        self.assertEqual('Null', 'Null') # If the input is "Null" the output is "Null"
        self.assertEqual('Hello', 'Bonjour') # If the input is "Hello" the output is "Bonjour"

    def french_to_english(self):
        self.assertEqual('Null', 'Null') # If the input is "Null" the output is "Null"
        self.assertEqual('Hello', 'Bonjour') # If the input is "Bonjour" the output is "Hello"

if __name__ == '__main__':
    unittest.main()