def mergeSort(array):
	helper = [0] * len(array)
	mergeSortMinMax(array, helper, 0, len(array) - 1)

def mergeSortMinMax(array, helper, min, max):
	if min < max:
		middle = int((min + max) / 2)
		mergeSortMinMax(array, helper, min, middle)
		mergeSortMinMax(array, helper, middle + 1, max)
		merge(array, helper, min, middle, max)

def merge(array, helper, min, middle, max):
	for i in range(min, max + 1):
		helper[i] = array[i]
		
	helperLeft = min
	helperRight = middle + 1
	current = min
	
	while helperLeft <= middle and helperRight <= max:
		if helper[helperLeft] <= helper[helperRight]:
			array[current] = helper[helperLeft]
			helperLeft += 1
		else:
			array[current] = array[helperRight]
			helperRight += 1
			
		current += 1
		
	remaining = middle - helperLeft
	
	for i in range(0, remaining + 1):
		array[current + i] = helper[helperLeft + i]
		
array = [5, 4]
mergeSort(array)
print(array)

array = [5, 4, 6]
mergeSort(array)
print(array)

array = [5, 4, 6, 5, 4, 6]
mergeSort(array)
print(array)

array = [7, 5, 4, 6, 5, 4, 6, 1]
mergeSort(array)
print(array)

array = [1, 2, 3, 4, 5, 6, 7]
mergeSort(array)
print(array)

array = [8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(array)
print(array)