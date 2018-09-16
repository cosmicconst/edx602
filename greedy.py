class Item(object):
    def __init__(self,name,value,cost):
        self.name = name
        self.value = value
        self.cost = cost
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getCost(self):
        return self.cost
    def getDensity(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return ("Name: " + self.getName() + " Cost: " + str(self.getCost()) + " Value: " + str(self.getValue()))


food = ["wine","beer","pizza","burger","fries","coke","apple","donut"]
value = [89,90,95,100, 90,79,90,10]
calories = [123,154,258,354,365,150,95,195]

def buildmenu(food,value,calories):
    menu = []
    for i in range(len(food)):
        menu.append(Item(food[i],value[i],calories[i]))
    return menu

items = buildmenu(food,value,calories)
for item in items:
    print(item)

def greedy(items, maxCost, keyfunction):
    sortitems = sorted(items, key = keyfunction, reverse=True)
    resultItems = []
    totalValue = 0.0
    totalCost = 0.0
    for i in range(len(sortitems)):
        if sortitems[i].getCost() + totalCost <= maxCost:
            resultItems.append(sortitems[i])
            totalCost += sortitems[i].getCost()
            totalValue += sortitems[i].getValue()
        else:
            break
    return (resultItems,totalValue)

def testgreedy(items, constraint, functionkey):
    taken, val = greedy(items, constraint,functionkey)
    print("Total number of items : " + str(len(taken)))
    print("Maxvalue of items: " + str(val))
    for item in taken:
        print(item)


def testgreedys(items,maxUnits):
    print('Use greedy by Value to allocate ',str(maxUnits), ' calories')
    testgreedy(items,maxUnits,Item.getValue)
    print('Use greedy by Cost to allocate ',str(maxUnits),' calories')
    testgreedy(items,maxUnits, lambda x: 1/Item.getCost(x))
    print("Use greedy by Density to allocate ", str(maxUnits), " calories")
    testgreedy(items,maxUnits,Item.getDensity)

testgreedys(items,750)
