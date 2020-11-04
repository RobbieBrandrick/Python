import unittest

def binarySearch(array, value):

    if len(array) == 0:
        return False

    middle = int(len(array) / 2)

    if array[middle] == value:
        return True

    if array[middle] > value:
        return binarySearch(array[:middle], value)

    if array[middle] < value:
        return binarySearch(array[middle + 1:], value)

class TestBinarySearch(unittest.TestCase):

    def test_one_element_array(self):
        array = [1]

        self.assertTrue(binarySearch(array, 1))
        self.assertFalse(binarySearch(array, 2))
        self.assertFalse(binarySearch(array, 0))

    def test_two_element_array(self):

        array = [1, 2]

        self.assertTrue(binarySearch(array, 1))
        self.assertTrue(binarySearch(array, 2))
        self.assertFalse(binarySearch(array, 3))
        self.assertFalse(binarySearch(array, 0))

    def test_three_element_array(self):

        array = [1, 2, 3]

        self.assertTrue(binarySearch(array, 1))
        self.assertTrue(binarySearch(array, 2))
        self.assertTrue(binarySearch(array, 3))
        self.assertFalse(binarySearch(array, 4))
        self.assertFalse(binarySearch(array, 0))        

    def test_four_element_array(self):

        array = [1, 2, 3, 4]

        self.assertTrue(binarySearch(array, 1))
        self.assertTrue(binarySearch(array, 2))
        self.assertTrue(binarySearch(array, 3))
        self.assertTrue(binarySearch(array, 4))
        self.assertFalse(binarySearch(array, 5))
        self.assertFalse(binarySearch(array, 0))              

    def test_five_element_array(self):

        array = [1, 2, 3, 4, 5]

        self.assertTrue(binarySearch(array, 1))
        self.assertTrue(binarySearch(array, 2))
        self.assertTrue(binarySearch(array, 3))
        self.assertTrue(binarySearch(array, 4))
        self.assertTrue(binarySearch(array, 5))
        self.assertFalse(binarySearch(array, 6))
        self.assertFalse(binarySearch(array, 0))              

    def test_five_element_array_random_numbers(self):

        array = [1, 8, 13, 54, 95]

        self.assertTrue(binarySearch(array, 1))
        self.assertTrue(binarySearch(array, 8))
        self.assertTrue(binarySearch(array, 13))
        self.assertTrue(binarySearch(array, 54))
        self.assertTrue(binarySearch(array, 95))
        self.assertFalse(binarySearch(array, 6))
        self.assertFalse(binarySearch(array, 0))               

if __name__ == '__main__':
    unittest.main()