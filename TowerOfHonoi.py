steps=0
peglist = [[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],[10,1]]
#peglist = [[1,1],[2,1],[3,1],[4,1],[5,1]]
#peglist = [[1,1],[2,1],[3,1]]
print("beginning: ",peglist)

def pegMove(peglist,target):
    global steps
    if len(peglist) == 0:
        return peglist
    elif len(peglist) == 1:
        peglist[0][1] = target
        print(peglist[0])
        steps += 1
        return peglist
    elif len(peglist) == 2:
            peglist[0][1] = tempPos(peglist[0][1],target)
            print(peglist[0])
            steps += 1
            peglist[1][1] = target
            print(peglist[1])
            steps += 1
            peglist[0][1] = target
            print(peglist[0])
            steps += 1
            return peglist
    else:
        pegMove(peglist[0:-1],tempPos(peglist[0][1],target))
        pegMove(peglist[-1:],target)
        pegMove(peglist[0:-1],target)
        return peglist

def tempPos(current, target):
    if current == 1 and target == 2:
        return 3
    elif current == 1 and target == 3:
        return 2
    elif current == 2 and target == 3:
        return 1
    elif current == 2 and target == 1:
        return 3
    elif current == 3 and target == 1:
        return 2
    elif current == 3 and  target == 2:
        return 1



print("ending:",pegMove(peglist,3))
print("steps:", steps)
