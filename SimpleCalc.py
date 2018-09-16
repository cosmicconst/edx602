listOfNum = []
try:
    while True:
        temp = input("enter a number or Enter to finish: ")
        if temp != '':
            listOfNum.append(int(temp))
        else:
            break
    Sum = 0
    for i in listOfNum:
        Sum += i
    print(listOfNum)
    print("Count: " + str(len(listOfNum)))
    print("Lowest: " + str(min(listOfNum)))
    print("Highest: " + str(max(listOfNum)))
    print("Average: " + str(Sum/len(listOfNum))) 
except:
    print("not acceptable entry")
    

    
