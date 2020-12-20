import unittest

def rotate_matrix(matrix):
    
    newMatrix = []

    for x in range(len(matrix[0])):
        newMatrix.append([])
        for y in range(len(matrix) - 1, -1, -1):        
            newMatrix[x].append(matrix[y][x])

    return newMatrix

class TestRotateMatrix(unittest.TestCase):
    
    def test_rotate_matrix(self):
        matrix = [[1, 2], 
                  [3, 4]]
        expected = [[3, 1],
                    [4, 2]]

        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        matrix = [[1, 2]]
        expected = [[1], [2]]

        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        matrix = [[1], [2]]
        expected = [[2, 1]]

        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        matrix = [[1], [2]]
        expected = [[1], [2]]

        matrix = rotate_matrix(matrix)
        matrix = rotate_matrix(matrix)
        matrix = rotate_matrix(matrix)
        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        matrix = [[1, 2, 3], 
                 	    [4, 5, 6],
                 	    [7, 8, 9]]
        expected = [[7, 4, 1],
        					 [8, 5, 2],
        					 [9, 6, 3]]

        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        expected = matrix
        
        result = rotate_matrix(result)
        result = rotate_matrix(result)
        result = rotate_matrix(result)
        
        self.assertEqual(result, expected)
        matrix = [[1, 2, 3],
        				[4, 5, 6]]
        				
        expected = [[4, 1],
        					[5, 2], 
        					[6, 3]]

        result = rotate_matrix(matrix)

        self.assertEqual(result, expected)
        
        expected = matrix
        
        result = rotate_matrix(result)
        result = rotate_matrix(result)
        result = rotate_matrix(result)
        
        self.assertEqual(result, expected)

unittest.main()

# matrix = [[1, 2], 
#             [3, 4]]

# rotate_matrix(matrix)