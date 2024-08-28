#9618/42/O/N/22
for _ in range(100):
    Jobs = [-1, -1] 
NumberOfJobs = 0  

def Initialise():
    global Jobs, NumberOfJobs
    Jobs = [[-1, -1] for _ in range(100)]
    NumberOfJobs = 0

def AddJob(job_number, priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs < 100: 
        Jobs[NumberOfJobs][0] = job_number
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs += 1
        print("Added in the array")
    else:
        print("cannot be added")

def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        key = Jobs[i]
        j = i - 1
        while j >= 0 and key[1] < Jobs[j][1]:
            Jobs[j + 1] = Jobs[j]
            j -= 1
        Jobs[j + 1] = key

def PrintArray():
    global Jobs, NumberOfJobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

def main():
    Initialise()

    AddJob(12, 10)
    AddJob(526, 9)
    AddJob(33, 8)
    AddJob(12, 9)
    AddJob(78, 1)

    InsertionSort()
    PrintArray()

if __name__ == '__main__':
    main()
