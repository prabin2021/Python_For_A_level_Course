# 9618/43/O/N/23
# (a) (i)
Queue = [""] * 50

HeadPointer = -1
TailPointer = 0

# (a) (ii)
def Enqueue(id_str):
    global TailPointer
    global HeadPointer

    if TailPointer >= 50:
        print("Queue is already full.")
    else:
        Queue[TailPointer] = id_str
        if HeadPointer == -1:
            HeadPointer = 0
        TailPointer += 1

# (a) (iii)

def Dequeue():
    global HeadPointer
    global TailPointer

    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue has nothing.")
        return "khali"
    else:
        first_element = Queue[HeadPointer]
        HeadPointer += 1
        if HeadPointer == TailPointer:
            HeadPointer = -1
            TailPointer = 0
        return first_element

#(b)

def ReadData():
    global TailPointer
    global HeadPointer
    with open("QueueData.txt", "r") as file:
        for line in file:
            id_str = line.strip()
            Enqueue(id_str)

#(c (i)

class RecordData:
    def __init__(self, id_str):
        self.ID = id_str  # store game ID
        self.Total = 1    #the total number of times the game ID appears

# (c) (ii)

Records = [None] * 50
NumberRecords = 0 
# (c) (iii)
def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False

    if DataAccessed == "khali":
        return

    if NumberRecords == 0:
        Records[NumberRecords] = RecordData(DataAccessed)
        Flag = True
        NumberRecords += 1
    else:
        for i in range(NumberRecords):
            if Records[i].ID == DataAccessed:
                Records[i].Total += 1
                Flag = True
                break

    if not Flag:
        Records[NumberRecords] = RecordData(DataAccessed)
        NumberRecords += 1

if __name__ == "__main__":
    ReadData()
    
    while HeadPointer != -1:
        TotalData()

    for record in Records:
        if record is not None:
            print(f"Game ID: {record.ID}, Total: {record.Total}")
