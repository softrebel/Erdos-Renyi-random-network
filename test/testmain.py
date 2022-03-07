import unittest
from src.main import create_edos_renyi_random_graph
class TestMain(unittest.TestCase):

    def test_erdos_renyi_random_network(self):
        p=0.005
        N=1000
        res=create_edos_renyi_random_graph(p,N)
        self.assertEqual(res, True)

    

if __name__ == '__main__':
    unittest.main()