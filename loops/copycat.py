#aim: to create a program that repeats user input until 
#"STOP COPYING ME" is the user input

user_input = input("Hey, how's it going? ")
while user_input != "STOP COPYING ME":
	user_input = input(f"{user_input}\n")
print("Fine! You win. Poopy pants.")