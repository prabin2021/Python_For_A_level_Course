
# def RecursiveInsertion(NumberArray,NumberElements):
#
#     if NumberElements <= 1:
#         return NumberArray
#     else:
#         RecursiveInsertion(NumberArray,NumberElements-1)
#         LastItem = NumberArray[NumberElements-1]
#         CheckItem = NumberElements-2
#     LoopAgain = True
#     if CheckItem < 0:
#         LoopAgain = False
#     else:
#         if NumberArray[CheckItem] < LastItem:
#             LoopAgain = False
#     while LoopAgain:
#         NumberArray[CheckItem+1] = NumberArray[CheckItem]
#         CheckItem = CheckItem-1
#         if CheckItem < 0:
#             LoopAgain = False
#         else:
#             if NumberArray[CheckItem] < LastItem:
#                 LoopAgain = False
#     NumberArray[CheckItem+1] = LastItem
#     return NumberArray
#
#
# def main():
#     IterativeInsertion(NumberArray,7)
#     print('Iterative')
#     print(NumberArray)
#
#
# def IterativeInsertion(NumberArray,NumberElements):
#     if NumberElements <= 1:
#         return NumberArray
#     else:
#         LastItem = NumberArray[NumberElements-1]
#         CheckItem = NumberElements-2
#     LoopAgain = True
#     if CheckItem < 0:
#         LoopAgain = False
#     else:
#         if NumberArray[CheckItem] < LastItem:
#             LoopAgain = False
#     while LoopAgain:
#         NumberArray[CheckItem+1] = NumberArray[CheckItem]
#         CheckItem = CheckItem-1
#         if CheckItem < 0:
#             LoopAgain = False
#         else:
#             if NumberArray[CheckItem] < LastItem:
#                 LoopAgain = False
#         NumberArray[CheckItem+1] = LastItem
#         NumberElements -= 1
#     return NumberArray
#
#
#
#
# main()
def BSearch(NumberArray, First, Last, ToFind):
    if First >= Last:
        print( NumberArray, First, Last, ToFind)
        mid=(Last+First)//2
        if ToFind == NumberArray[mid]:
            return mid
        elif ToFind < NumberArray[mid]:
            return BSearch(NumberArray, First, mid-1, ToFind)
        else:
            return BSearch(NumberArray, mid+1, Last, ToFind)
    else:
        return -1

NumberArray=[100,85,644,22,15,8,1]
First = 0
ToFind = 85
Last = 6
position=BSearch(NumberArray,First,Last,ToFind)
print(position)

