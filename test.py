import unittest
from main import to_upper

class Mytestcase(unittest.TestCase):
    def test_upper(self):
        name="Jannat 6634"
        upper=to_upper(name)
        self.assertEqual(upper, "Jannat 6634")

if __name__ == '__main__':
    unittest.main()