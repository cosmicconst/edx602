import random


rows = int(input("row: "))
columns = int(input("columns: "))
minimum = input("minimum (or Enter for 0): ")
maximum = input("maximum (or Enter for 1000): ")
if minimum == '':
    minimum = 0
else:
    minimum = int(minimum)
if maximum == '':
    maximum = 1000
else:
    maximum = int(maximum)
for row in range(rows):
    for col in range(columns):
        randomNum = random.randint(minimum, maximum)
        print(str(randomNum), end=" ")
    print()
