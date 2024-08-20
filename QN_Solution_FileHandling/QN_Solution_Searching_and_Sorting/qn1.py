

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(value):
    for item in arrayData:
        if item == value:
            return True
    return False

def bubbleSort():
    global arrayData
    n = len(arrayData)
    for x in range(n):
        for y in range(n - x - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp

def main():
    global arrayData
    print("Array initialized:", arrayData)
    value = int(input("Enter an integer to search: "))
    found = linearSearch(value)
    if found:
        print(f"The value {value} was found in the array.")
    else:
        print(f"The value {value} was not found in the array.")

    print("Sorting array in descending order...")
    bubbleSort()
    print("Sorted array:", arrayData)

if __name__ == "__main__":
    main()
