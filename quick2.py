def partition(arr, low, high):

    #setting the pivot
    pivot = arr[(low + high) // 2]

    i = low 
    j = high

    while i < j:
        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

            
    arr[j], arr[i] = arr[i], arr[j]     
    return j

def quicksort(low, high):
    if low < high:
        j = partition(low, high)
        quicksort(low, j)
        quicksort(j + 1, high)
        