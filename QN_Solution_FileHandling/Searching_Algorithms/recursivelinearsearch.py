def search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)

arr = [4, 2, 3, 7, 8, 9]
key = int(input("Enter any number to search"))
curr_index = len(arr) - 1
result = search(arr, curr_index, key)
if result == -1:
    print(f"{key} not found")
else:
    print(f"{key} found at {result} index.")
