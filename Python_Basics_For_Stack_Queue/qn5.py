# 9618/41/on/23
HeadPointer = -1   
TailPointer = 0   

def Enqueue(item):
    global TailPointer, Queue
    global HeadPointer
    if TailPointer >= len(Queue):#50
        print("The queue is full.")
    else:
        if TailPointer == 0:
            HeadPointer = 0
        Queue[TailPointer] = item
        TailPointer += 1

def Dequeue():
    global HeadPointer, TailPointer, Queue
    if HeadPointer == -1 or HeadPointer >= TailPointer:
        print("The queue is empty.")
        return "Empty"
    else:
        dequeued_item = Queue[HeadPointer]
        HeadPointer += 1
        return dequeued_item

def ReadData():
    try:
        with open("QueueData.txt", "r") as file:
            for line in file:
                item = line.strip()
                Enqueue(item)
    except FileNotFoundError:
        print("The file QueueData.txt was not found.")

class RecordData:
    def __init__(self, ID, Total=1):
        self.ID = ID  
        self.Total = Total  

Records = [None] * 50  
NumberRecords = 0
def TotalData():
    global NumberRecords, Records
    DataAccessed = Dequeue()
    Flag = False

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

def OutputRecords():
    global NumberRecords, Records
    for i in range(NumberRecords):
        if Records[i]:
            print(f"ID {Records[i].ID} Total {Records[i].Total}")

def main():
    ReadData()
    for i in range(TailPointer - HeadPointer):
        TotalData()
    OutputRecords()

if __name__ == "__main__":
    main()
