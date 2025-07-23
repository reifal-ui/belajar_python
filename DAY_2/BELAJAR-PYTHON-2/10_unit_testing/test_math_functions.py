import unittest

def tambah(a, b):
    return a + b

class TestTambah(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(tambah(2, 3), 5)

if __name__ == '__main__':
    unittest.main()