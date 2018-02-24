#assigning a random choice to the computer opponent
from random import randint

computer = randint(0,2)

if computer == 0:
	computer = "rock"
elif computer == 1:
	computer = "scissors"
else:
	computer = "paper"

print("...rock...\n...scissors...\n...paper...\n")

#player 1 entering their choice
player = input("enter your choice: ").lower()

#checking to see if entered a valid choice
while player != "rock" and player != "paper" and player != "scissors":
		player = input("please enter a valid choice: ")

#printing what the computer was randomly assigned
print(f"The computer was assigned: {computer}")

#checking who wins		
if player == computer:
	print("DRAW")

elif player == "rock":
	if computer == "scissors":
		print("Player 1 wins")
	else:
		print("Player 2 wins")

elif player == "paper":
	if computer == "scissors":
		print("Player 2 wins")
	else:
		print("Player 1 wins")

elif player == "scissors":
	if computer == "rock":
		print("Player 2 wins")
	else:
		print("Player 1 wins")

else:
	print("Not a legitimate game")