#Dungeons and Dragons Dice Roller
import random


def display_results(diceTotal, diceResults):
    result = ""
    for x in diceResults:
        result += ("{} ".format(x))
    print("---------------------------------------------------------------")
    print("Total: {}. Results by Dice: {}" .format(diceTotal, result))
    print("---------------------------------------------------------------")

#Getting numbers for dice- in front is number ofdices, inBack is no. of sides of each dice
def get_random_numbers(inFront, inBack):
    inFront = int(inFront)
    inBack = int(inBack)
    diceTotal = 0
    diceResults = []

    for x in range(int(inFront)):
        dice_roll = random.randint(1,inBack)
        diceTotal += dice_roll
        diceResults.append(dice_roll)

    return diceTotal, diceResults

def user_input():
    userInput = input("\nEnter number of dices and sides in format - [Number]d[Sides]:  ")
    return userInput

#Check in front and in back od letter d for numbers
#Get numbers in front and in back of "d"
def check_for_numerical(userInput):
    inFront = ""
    inBack = ""
    resultFront = "OK"
    resultBack = "OK"
    foundD = False

    for x in userInput:
        if x != "d" and foundD == False:
            inFront += str(x)
        #if its "d" for the first time, else add it in back
        elif x == "d" and foundD == False:
            foundD = True
            continue
        elif foundD == True:
            inBack += str(x)

    if not inFront.isnumeric():
        resultFront = "NOT"

    if not inBack.isnumeric():
        resultBack = "NOT"


    #print("front "+inFront)
    #print("back "+inBack)
    return userInput, resultFront, resultBack, inFront, inBack




def main():

    while True:

        userInput = user_input()

        if userInput.lower() == "x":
            print("---------------------------------------------------------------")
            print("Good bye.")
            break

        elif "d" not in userInput:
            print("Your D&D dices are missing letter 'd' ! Try again.")
            print("---------------------------------------------------------------")

        userInput, resultFront, resultBack, inFront, inBack = check_for_numerical(userInput)

        if resultFront == "NOT":

            print("You don't have only numbers in front of letter 'd'. Try again.")
            print("---------------------------------------------------------------")

        if resultBack == "NOT":
            print("You don't  have only numbers in back of letter 'd'. Try again.")
            print("---------------------------------------------------------------")
        if resultFront == "OK" and resultBack == "OK":
            diceTotal, diceResults = get_random_numbers(inFront, inBack)


            display_results(diceTotal, diceResults)


if __name__ == "__main__":
    main()