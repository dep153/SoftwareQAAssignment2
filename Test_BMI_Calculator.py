import unittest
from BMI_Calculator import BMI_Calc

class BMI_Test_Case(unittest.TestCase):
    def test_BMI_Calculation(self):
        BMI = BMI_Calc(6, 0, 160)
        self.assertEqual(BMI, 22.2)
