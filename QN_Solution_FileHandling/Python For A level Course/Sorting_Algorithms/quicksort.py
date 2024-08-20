def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


arr = [6,4,7,8,2,1,4,5,0]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
