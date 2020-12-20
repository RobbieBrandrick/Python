import unittest

def rotate_matrix(matrix):

    matrixLength = len(matrix[0]) - 1

    maxLayers = 1 if matrixLength < 2 else matrixLength - 1

    for layer in range(0, maxLayers):

        beginLayer = layer
        endLayer = matrixLength - layer
        
        for i in range(0, endLayer - beginLayer):

            beginIndex = beginLayer + i
            endIndex = endLayer - i

            n = matrix[beginLayer][beginIndex]  #North Position
            e = matrix[beginIndex][endLayer]    #East Position
            s = matrix[endLayer][endIndex]      #South Position
            w = matrix[endIndex][beginLayer]    #West Position

            matrix[beginLayer][beginIndex]  = w #North Position
            matrix[beginIndex][endLayer]    = n #East Position
            matrix[endLayer][endIndex]      = e #South Position
            matrix[endIndex][beginLayer]    = s #West Position 

class TestRotateMatrix(unittest.TestCase):
    
    def test_rotate_matrix_2x2(self):
        matrix = [
            [1, 2], 
            [3, 4]
        ]

        expected = [
            [3, 1],
            [4, 2]
        ]

        rotate_matrix(matrix)

        self.assertEqual(matrix, expected)
    
    def test_rotate_matrix_3x3(self):

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]

        rotate_matrix(matrix)

        self.assertEqual(matrix, expected)        
    
    def test_rotate_matrix_4x4(self):

        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ]

        rotate_matrix(matrix)

        self.assertEqual(matrix, expected)          

    def test_rotate_matrix_5x5(self):

        matrix = [
            [0, 1, 2, 3, 4], 
            [5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14], 
            [15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24]
        ]

        expected = [
            [20, 15, 10, 5, 0],
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4]
        ]        

        rotate_matrix(matrix)

        self.assertEqual(matrix, expected)

    def test_rotate_matrix_5x5_4rotations(self):

        matrix = [
            [0, 1, 2, 3, 4], 
            [5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14], 
            [15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24]
        ]

        expected = [
            [0, 1, 2, 3, 4], 
            [5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14], 
            [15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24]
        ]

        rotate_matrix(matrix)
        self.assertNotEqual(matrix, expected)  
        
        rotate_matrix(matrix)
        self.assertNotEqual(matrix, expected)  

        rotate_matrix(matrix)
        self.assertNotEqual(matrix, expected)  
        
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)             


unittest.main()
