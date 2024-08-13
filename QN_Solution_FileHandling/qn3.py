Animal = [""] * 20
Colour = [""] * 10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer -= 1
        return Animal[AnimalTopPointer]


def ReadData():
    try:
        with open('AnimalData.txt', 'r') as file:
            for i in file:
                PushAnimal(i.strip())
    except FileNotFoundError:
        print("AnimalData.txt not found. Please try again")


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer -= 1
        return Colour[ColourTopPointer]


def ReadData():
    try:
        with open('AnimalData.txt', 'r') as file:
            for line in file:
                line = line.strip()
                PushAnimal(line)
    except FileNotFoundError:
        print("AnimalData.txt not found. Please try again")

    try:
        with open('ColourData.txt', 'r') as file:
            for line in file:
                line = line.strip()
                PushColour(line)
    except FileNotFoundError:
        print("ColourData.txt is not found. Please try again")


def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    
    if colour == "":
        if animal != "":
            PushAnimal(animal)
        print("No colour")
    elif animal == "":
        if colour != "":
            PushColour(colour)
        print("No animal")
    else:
        print(f"{colour} {animal}")


def main():
    ReadData()
    for _ in range(4):
        OutputItem()

if __name__ == "__main__":
    main()
