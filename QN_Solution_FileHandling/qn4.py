class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer  #str
        self.__points = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, user_answer):
        return user_answer == self.__answer  ##striplower

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or 4:

            return self.__points // 4
        else:
            return 0

def readData():
    arrayTreasure = []
    try:
        with open('TreasureChestData.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                question = lines[i].strip()
                answer = int(lines[i+1].strip())
                points = int(lines[i+2].strip())
                treasure_chest = TreasureChest(question, answer, points)
                arrayTreasure.append(treasure_chest)
    except FileNotFoundError:
        print("File not found. Please make sure 'TreasureChestData.txt' exists.")
    return arrayTreasure

def main():
    treasures = readData()
    if not treasures:
        return
    
    question_num = int(input("Enter a question number between 1 and 5: ")) - 1
    if question_num < 0 or question_num >= len(treasures):
        print("Invalid question number.")
        return
    
    treasure = treasures[question_num]  #using obj
    attempts = 0
    correct = False
    
    while not correct:
        attempts += 1
        print(treasure.getQuestion())
        user_answer = int(input("Enter your answer: "))
        correct = treasure.checkAnswer(user_answer)
        if not correct:
            print("Incorrect answer, try again.")
    
    points_awarded = treasure.getPoints(attempts)
    print(f"Correct! You are awarded {points_awarded} points after {attempts} attempts.")

if __name__ == "__main__":
    main()
