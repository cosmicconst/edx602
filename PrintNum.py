import sys
one = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]
two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]
three = ["*** ",
         "   *",
         "   *",
         "****",
         "   *",
         "   *",
         "*** "]
four = ["   *  ",
        "  **  ",
        " * *  ",
        "*  *  ",
        "******",
        "   *  ",
        "   *  "]
five = [" **** ",
        "*     ",
        "*     ",
        " **** ",
        "     *",
        "     *",
        " **** "]
six = ["    *",
       "    *",
       "    *",
       " ****",
       "*   *",
       "*   *",
       " *** "]
seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *"]
zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
numDict = {'1':one,'2':two,'3':three,'4':four,'5':five,'6':six,'7':seven,'8':eight,'9':nine,'0':zero}

try:
    digits = sys.argv[1]
    for i in range(7):
        for num in digits:
            #version 1 print * for the pattern
            #print(numDict[num][i],end= ' ')
            #version 2 print the number for the pattern
            for char in numDict[num][i]:
                if char == '*':
                    char = int(num)
                print(char, end='')
            print(end=' ')
        print()
except IndexError:
    print("usage: PrintNum <Number>")
except ValueError as err:
    print(err,"in", digits)
    
