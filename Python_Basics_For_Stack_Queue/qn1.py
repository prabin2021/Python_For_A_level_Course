# 9618/43/O/N/23

# Iterative function to count the number of lowercase vowels in a string
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter in 'aeiou':
            Total += 1
        Value = Value[1:]
    return Total

# Recursive function to count the number of lowercase vowels in a string
def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if FirstCharacter in 'aeiou':
            return 1 + RecursiveVowels(Value[1:])
        else:
            return 0 + RecursiveVowels(Value[1:])

# Main program to call and test the functions
if __name__ == "__main__":
    # Testing IterativeVowels with the string "house"
    result_iterative = IterativeVowels("house")
    print("Number of vowels in 'house' (Iterative):", result_iterative)
    
    # Testing RecursiveVowels with the string "imagine"
    result_recursive = RecursiveVowels("imagine")
    print("Number of vowels in 'imagine' (Recursive):", result_recursive)


