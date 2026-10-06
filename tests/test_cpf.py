import unittest

from store.cpf import is_valid_cpf


class CpfTest(unittest.TestCase):
    def test_valid_cpf(self):
        self.assertTrue(is_valid_cpf("529.982.247-25"))

    def test_wrong_check_digits(self):
        self.assertFalse(is_valid_cpf("123.456.789-00"))

    def test_wrong_length(self):
        self.assertFalse(is_valid_cpf("123"))


if __name__ == "__main__":
    unittest.main()
