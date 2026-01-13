def quicksort(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[len(arr) // 2]
	middle = [x for x in arr if x == pivot]
	left = [x for x in arr if x < pivot]
	right = [x for x in arr if x > pivot]

	return quicksort(left) + middle + quicksort(right)

nums = [8,3,1,7,0,10,2]
print(quicksort(nums))


