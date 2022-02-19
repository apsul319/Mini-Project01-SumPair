from logging import exception


def pairSum(x, upper, lower): # Generates a consecutive list of pairs for the specified number "x"
    combo = []
    for i in range(lower, upper+1, 1):
        for j in range(i+1, upper+1, 1):
            if i + j == x:
                combo.append(f"{i} and {j}")
    if len(combo) == 0:
        return combo.append("NONE")
    return combo

validRange = False

while not validRange: # Loop ensures user inputs a valid upper and lower limit without error
    try:
        up = int(input("Choose an upper limit (inclusive)\n"))
    except ValueError:
        up = None
        print("Enter an INT")
    else:
        try:
            low = int(input("Choose a lower limit\n"))
        except ValueError:
            low = None
            print("Enter an INT")
        else:
            if up > low:
                validRange = True
            else:
                print("Be sure the upper limit is greater than the lower limit")

finishSet = False
numSet = set()

while not finishSet: # Loop ensures user inputs as many numbers as requested into the set until specified otherwise by inputting "q"
    num = input("Type a number to put into the set. Enter \"q\" to quit\n")
    try:
        num = int(num)
    except ValueError:
        if isinstance(num, str) and num == "q":
            finishSet = True
        else:
            print("Invalid input")
    else:
        if num >= low and num <= up:
            numSet.add(num)
        else:
            print("Number is not within set parameters")
print()
for val in sorted(numSet): # For loop prints each unique number value entered into the set along with all unique pairs of numbers that were calculated within the specified range
    print(f"Pairs within {val}: {pairSum(val, up, low)}\n")

