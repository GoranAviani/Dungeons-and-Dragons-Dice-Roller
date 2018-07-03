#Dungeons and dragons dice simulator
def user_input():
    userInput = input("Enter number of dices and sides in format - [Number]d[Sides]:  ")
    return userInput

#Check in front and in back od letter d for numbers
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


    print("front "+inFront)
    print("back "+inBack)
    return userInput, resultFront, resultBack




def main():

    while True:

        userInput = user_input()

        if userInput.lower() == "x":
            print("Good bye.")
            break

        elif "d" not in userInput:
            print("Your D&D dices are missing letter 'd' ! Try again.")

        userInput, resultFront, resultBack = check_for_numerical(userInput)

        if resultFront == "NOT":
            print("You don't only have numbers infront of letter 'd'. Try again.")

        if resultBack == "NOT":
            print("You don't only have numbers inback of letter 'd'. Try again.")



if __name__ == "__main__":
    main()