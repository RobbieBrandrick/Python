import unittest

def transpose_matrix(matrix):

    matrixLength = len(matrix[0])

    for y in range(0, matrixLength):

        for x in range(y, matrixLength):

            temp = matrix[y][x]
            matrix[y][x] = matrix[x][y]
            matrix[x][y] = temp

class TestTransposeMatrix(unittest.TestCase):
    
    def test_transpose_5x5(self):
        matrix = [
            [0, 1, 2, 3, 4], 
            [5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14], 
            [15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24]
        ]

        expected = [
            [0, 5, 10, 15, 20],
            [1, 6, 11, 16, 21],
            [2, 7, 12, 17, 22],
            [3, 8, 13, 18, 23],
            [4, 9, 14, 19, 24],
        ]       

        transpose_matrix(matrix)

        self.assertEqual(matrix, expected)

unittest.main()