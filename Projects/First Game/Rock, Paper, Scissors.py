#This is Pratice for you Chandler get it done Fam!

from random import randint

ComputerScore = 0
PlayerScore = 0

#List of Moves
M = ["Rock","Paper","Scissors"]

#Setting the Computer to an Random Int
Computer = M[randint(0,2)]

#setting the player to false to make a loop
Player = False

while Player == False:
    Player = input("Rock,Paper,Scissors?:")
    if Player == Computer:
        print("WE TIED...CAUSE I WANT TO MAKE IT SEEM LIKE YOU CAN WIN")
    elif Player == "Rock":
        if Computer == "Paper":
            ComputerScore += 1
            print("YOU LOSE",Computer,"Wrapped You Up",Player)
        else:
            PlayerScore += 1
            print("YOU WON...Somehow",Player,"Monkey Stomped",Computer)
    elif Player == "Paper":
        if Computer == "Scissors":
            ComputerScore += 1
            print("YOU LOSE...Cause im a Smart PC dummy",Computer,"Shanked",Player)
        else:
            PlayerScore += 1
            print("YOU WON....WHAT YOUR CHEATING",Player,"SMOTHERED",Computer)
    elif Player == "Scissors":
        if Computer == "Rock":
            ComputerScore += 1
            print("YOU LOSE.....TRASH PLAYER",Computer,"CAVEMANED",Player)
        else:
            PlayerScore += 1
            print("YOU WON.....I LET YOU WIN THAT TIME",Player,"SLICED",Computer)
    else:
         print("YOU SPELT IT WRONG DINGUS")
    Player = False
    Computer = M[randint (0,2)]
    print("PLayerScore:",PlayerScore)
    print("ComputerScore:",ComputerScore)












