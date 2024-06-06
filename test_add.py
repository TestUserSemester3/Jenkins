import unittest
from add import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        print(f'Test add(3, 2): Expected 3, Got {add(2, 2)}')
        self.assertEqual(add(1, 2), 3)
        
        print(f'Test add(-2, 1): Expected 0, Got {add(-2, 1)}')
        self.assertEqual(add(-1, 1), 0)
        
        print(f'Test add(0, 0): Expected 0, Got {add(0, 0)}')
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
