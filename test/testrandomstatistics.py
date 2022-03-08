import unittest
from src.random_statistics import *
class TestRandomStatistics(unittest.TestCase):

    def test_calculate_s_by_lambert_w_function(self):
        mean_k=1.5
        result=0.5828116536140442
        res=calculate_s_by_lambert(mean_k)
        self.assertEqual(res, result)

    def test_calculate_s_by_curve_intersection(self):
        mean_k=1.5
        result=0.5807922135825879
        res=calculate_s_by_curves_intersections(mean_k)
        self.assertEqual(res[1], result)

    def test_calculate_k_max_probabilty(self):
        mean_k=1.5
        result=0.2510
        res=calculate_probability_k_max(1,mean_k)
        self.assertEqual(np.round(res,4), result)

    def test_test_calculate_k_max_from_guess(self):
        mean_k=5
        N=1000
        result=12
        res = calculate_kmax_from_guess(N,mean_k)
        self.assertEqual(res, result)

    def test_calculate_k_max_by_series(self):
        mean_k=5
        N=1000
        result=13
        res = calculate_k_max_by_series(N,mean_k)
        self.assertEqual(res, result)

    def test_calculate_s_by_binary_search(self):
        mean_k = 1.5
        result = 0.58282470703125
        res = calculate_s_by_binary_search(mean_k)
        self.assertEqual(res, result)

if __name__ == '__main__':
    unittest.main()