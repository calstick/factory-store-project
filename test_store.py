import unittest
from unittest.mock import patch
from store import calculate_total, prompt_float

class TestStore(unittest.TestCase):

	def test_standard_discount(self): 
		# A 20% discount on $100 should be $80
		self.assertEqual(calculate_total(100, 20), 80.0)

	def test_negative_discount_exploit(self):
		# If someone passess -50%, it should raise an error or cap it at 0
		# Right now this test WILL FAIL because our code lets negative numbers through
		with self.assertRaises(ValueError): 
			calculate_total(100, -50)

	def test_zero_discount(self):
		self.assertEqual(calculate_total(100, 0), 100.0)

	def test_full_discount(self):
		self.assertEqual(calculate_total(100, 100), 0.0)

	def test_discount_over_100_raises(self):
		with self.assertRaises(ValueError):
			calculate_total(100, 150)

	def test_negative_price_raises(self):
		with self.assertRaises(ValueError):
			calculate_total(-100, 20)

	def test_fractional_discount(self):
		self.assertAlmostEqual(calculate_total(50, 12.5), 43.75)


class TestPromptFloat(unittest.TestCase):

	@patch("builtins.input", return_value="42.5")
	def test_valid_input(self, _):
		self.assertEqual(prompt_float("> "), 42.5)

	@patch("builtins.input", side_effect=["abc", "10"])
	def test_retries_on_invalid_input(self, _):
		self.assertEqual(prompt_float("> "), 10.0)


if __name__ == "__main__":
	unittest.main()


