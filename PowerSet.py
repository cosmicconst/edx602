# The is a recursive function to generate a power set based on an list of items
# Input: List of items
# Return: List of a list of items with all possible combitions in no specific order

def genPowerset(items):
    if len(items) == 0:
        return [[]]
    else:
        curritem = []
        curritem.append(items[0])
        itemsret = genPowerset(items[1:])
        finallist = itemsret[:]
        for i in range(len(itemsret)):
            finallist.append(curritem + itemsret[i])
        return finallist


items = ['A','B','C','D','E','F','G','H','I','J']
retList = genPowerset(items)
for item in retList:
    print(item)
print(len(retList))

