#9618/42/O/N/23
StackVowel = [''] * 100 
StackConsonant = [''] * 100  

VowelTop = 0  
ConsonantTop = 0  

def PushData(letter):
    global StackVowel, StackConsonant, VowelTop, ConsonantTop
    vowels = 'aeiou'
    
    if letter in vowels:
        if VowelTop < 100:
            StackVowel[VowelTop] = letter
            VowelTop += 1
        else:
            print("StackVowel is already full.")
    else:
        if ConsonantTop < 100:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1
        else:
            print("StackConsonant is already full.")

def ReadData():
    try:
        with open('StackData.txt', 'r') as file:
            for line in file:
                for letter in line.strip():
                    PushData(letter)
    except FileNotFoundError:
        print("The file does not exist.")

def PopVowel():
    global VowelTop
    if VowelTop > 0:
        VowelTop -= 1
        return StackVowel[VowelTop]
    else:
        return "No data"

def PopConsonant():
    global ConsonantTop
    if ConsonantTop > 0:
        ConsonantTop -= 1
        return StackConsonant[ConsonantTop]
    else:
        return "No data"

def main():
    ReadData()
    returned_letters = []

    for _ in range(5):
        choice = input("Enter your choice (vowel/consonant): ").strip().lower()
        if choice == "vowel":
            letter = PopVowel()
        elif choice == "consonant":
            letter = PopConsonant()
        else:
            print("Invalid choice.")
            continue
        
        if letter == "No data":
            print("The stack is empty.")
            break
        
        returned_letters.append(letter)
    
    print("".join(returned_letters))

if __name__ == "__main__":
    main()
