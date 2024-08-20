DataArray = [0]*50
def ReadFile():
    try:
        with open('IntegerData.txt','r') as file:
            line = file.readlines()
            for i in range(min(len(line), 50)): 
                DataArray[i] = line[i].strip() 
    except FileNotFoundError:
        print("File not found")
ReadFile()
print(DataArray)