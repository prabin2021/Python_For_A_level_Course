#9618/42/M/J/22

# Global data structures
StackData = [0] * 10
StackPointer = 0

def output_stack():
    global StackData, StackPointer
    print("Stack contents:", StackData)
    print("StackPointer:", StackPointer)

def Push(value):
    global StackData, StackPointer
    if StackPointer >= 10:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer += 1
        return True

def Pop():
    global StackData, StackPointer
    if StackPointer <= 0:
        return -1
    else:
        # StackPointer -= 1
        # removed_data = StackData[StackPointer]
        # # StackData[StackPointer] = None
        # return removed_data
        StackPointer -= 1
        return StackData.pop()

def main():
    global StackData, StackPointer
    print("Testing Push() function.")

    # Allow the user to enter 11 numbers
    inputs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    for i in inputs:
        
        if Push(i):
            print(f"{i} is added to the stack.")
        else:
            print(f"{i} is not added to the stack. Stack is already full.")

    # Output the contents of the stack after attempting to add all 11 numbers
    output_stack()

    # Removing two elements using Pop() function
    print("Removing two elements using Pop() function.")
    pop1 = Pop()
    pop2 = Pop()
    print(f"Removed element: {pop1}")
    print(f"Removed element: {pop2}")

    # Output the updated contents of the stack
    output_stack()

main()
