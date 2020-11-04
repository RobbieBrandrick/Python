def quickSort(array):
	quickSortLeftRight(array, 0, len(array) - 1)

def quickSortLeftRight(array, left, right):
	index  = partition(array, left, right)
	
	if left < index - 1:
		quickSortLeftRight(array, left, index - 1)
	
	if index < right:
		quickSortLeftRight(array, index, right)
		
def partition(array, left, right):
	pivot = array[int((left + right) / 2)]
	
	while left <= right:
		
		while array[left] < pivot:
			left += 1
			
		while array[right] > pivot:
			right -= 1
			
		if left <= right:
			swap(array, left, right)
			left += 1
			right -= 1
			
	return left

def swap(array, left, right):
	temp = array[left]
	array[left] = array[right]
	array[right] = temp

array = [5]
quickSort(array)
print(array)	
			
array = [5, 4]
quickSort(array)
print(array)

array = [5, 4, 8, 9, 1]
quickSort(array)
print(array)

array = [1, 2, 3, 4, 5]
quickSort(array)
print(array)