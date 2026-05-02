import unittest
from taxi import escolhe_taxi
class Test(unittest.TestCase):
  def test_escolhe_taxi_teste(self):
    self.assertEqual(escolhe_taxi("2.5","1.0","5.0","0.75"), "Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0")