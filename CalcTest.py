import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_sub(self):
        calc = Calculator()
        res = calc.sub(5, 3)
        self.assertEqual(res, 2)  # Expect 5 - 3 = 2

    def test_mul(self):
        calc = Calculator()
        res1 = calc.mul(2, 3)
        res2 = calc.mul(-3, 3)
        self.assertEqual(res1, 6)  # Expect 2 * 3 = 6
        self.assertEqual(res2, -9)  # Expect 3.6 * 3 = -9

    def test_div(self):
        calc = Calculator()
        res1 = calc.div(6, 3)
        res2 = calc.div(7, 2)
        res3 = calc.div(10, 3)
        self.assertEqual(res1, 2.0)  # Expect 6 / 3 = 2.0
        self.assertEqual(res2, 3.5)  # Expect 7 / 2 = 3.5
        self.assertEqual(res3, 3.33)


if __name__ == "__main__":
    unittest.main()
