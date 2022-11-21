"""
Test of translation
"""
import unittest
from translator import english_to_french
from translator import french_to_english

class Teste2f(unittest.TestCase):
    """
    This class tests English to French
    """
    def e2f(self):
        """
        Method to test English to French
        """
        self.assertEqual(english_to_french(''), '')
        # If the input is "Null" the output is "Null"
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # If the input is "Hello" the output is "Bonjour"

class Testf2e(unittest.TestCase):
    """
    This class tests English to French
    """
    def f2e(self):
        """
        Method to test French to English
        """
        self.assertEqual(french_to_english(''), '')
        # If the input is "Null" the output is "Null"
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # If the input is "Bonjour" the output is "Hello"

if __name__ == '__main__':
    unittest.main()
