from unittest import TestCase, main
from currency_converter import convert1 as convert # Change this to whichever one you want to test

class TestCurrencyConverter(TestCase):
    def test_JPY_1(self):
        self.assertAlmostEqual(135, convert("JPY"), delta=0.01)
    
    def test_EGP_1(self):
        self.assertAlmostEqual(30.85, convert("EGP"), delta=0.01)
    
    def test_ARS_1(self):
        self.assertAlmostEqual(227.6, convert("ARS"), delta=0.01)
    
    def test_JPY_50(self):
        self.assertAlmostEqual(6_750, convert("JPY", 50), delta=0.01)
    
    def test_EGP_50(self):
        self.assertAlmostEqual(1_542.5, convert("EGP", 50), delta=0.01)
    
    def test_ARS_50(self):
        self.assertAlmostEqual(11_380, convert("ARS", 50), delta=0.01)
    
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            convert("ARS", -1)

    def test_unsupported_currency(self):
        with self.assertRaises(LookupError):
            convert("something else")

if __name__ == "__main__": main()