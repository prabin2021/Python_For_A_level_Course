
names = [''] * 11
scores = [0] * 11

def ReadHighScoresFun():
    global names, scores
    with open('HighScore.txt', 'r') as file:
        for i in range(10):
            line = file.readline().strip()
            name, score = line.split()
            names[i] = name
            scores[i] = int(score)

def OutputHighScoresFun():
    global names, scores
    for i in range(10):
        print(f"{names[i]} {scores[i]}")

def InsertNewScoreFun(name, score):
    global names, scores
    names[10] = name
    scores[10] = score

    # descending order maintain garne
    for i in range(10, 0, -1):
        if scores[i] > scores[i-1]:
        #Score swap garne
            scores[i], scores[i-1] = scores[i-1], scores[i]
            # names swap garne
            names[i], names[i-1] = names[i-1], names[i]

def WriteTopTenFun():
    global names, scores
    with open('NewHighScore.txt', 'w') as file:
        for i in range(10):
            file.write(f"{names[i]} {scores[i]}\n")

if __name__ == "__main__":
    ReadHighScoresFun()
    OutputHighScoresFun()
    
    new_name = input("Enter player name in 3 character: ")
    if len(new_name) == 3:
        scor = int(input("Enter the score between 1 and 100000: "))
        if scor >1 and scor < 100000:
            new_score = scor
        else:
            print("Enter valid score")
            pass
    else:
        print("Only input 3 character")
        pass
    
    print("Before.... ")
    OutputHighScoresFun()
    
    InsertNewScoreFun(new_name, new_score)
    
    print("After....")
    OutputHighScoresFun()
    
    WriteTopTenFun()


