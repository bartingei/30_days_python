def quicksort(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[len(arr)//2]
	middle = [x for x in arr if x == pivot]
	left = [x for x in arr if x < pivot]
	right = [x for x in arr if x > pivot]

	return quicksort(left) + middle + quicksort(right)

numbers = [87, 20, 100, 43, 222, 6, 12, 98, 33]

print(quicksort(numbers))
