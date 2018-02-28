# aim: make a number guessing game with the ability to play again if wanted

# importing randint 
from random import randint


again = "y"

while again == "y":

	#generating a random number
	random_number = randint(1,10)

	#user inputs their guess, converts to int
	guess = int(input("enter your guess (1-10): "))
	
	#logic loop to check guess, if the guess is correct the user wins, else user is asked to guess again
	while True:
		if guess == random_number:
			print("You win")
			break
		elif guess < 1 or guess > 10:
			guess = int(input("enter a number within the range: "))
		elif guess < random_number:
			guess = int(input("Too low, guess again: "))
		elif guess > random_number:
			guess = int(input("Too high, guess again: "))
		else:
			int(input("Not a valid number, guess again: "))

	#user is aked if they want to play again
	again = input("Do you want to play again? (y/n) ").lower()
	
	#checks to see if they entered a valid option
	while True:
		if again == "y" or again == "n":
			break
		else:
			again = input("Please enter valid option (y/n): ")