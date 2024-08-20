DataArray = [0] * 25
def read_data_from_file():
    with open('Data.txt', 'r') as file:
        lines = file.readlines()
        for i in range(25):
            DataArray[i] = int(lines[i].strip())

def PrintArray(array):
    for item in array:
        print(item, end=' ')
    print()

def LinearSearch(array, search_value):
    count = 0
    for item in array:
        if item == search_value:
            count += 1
    return count

def main():
    global DataArray 
    read_data_from_file()
    PrintArray(DataArray)

    while True:
        try:
            user_input = int(input("Enter a whole number between 0 and 100 inclusive: "))
            if 0 <= user_input <= 100:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    result = LinearSearch(DataArray, user_input)
    print(f"The number {user_input} is found {result} times.")

if __name__ == "__main__":
    main()
