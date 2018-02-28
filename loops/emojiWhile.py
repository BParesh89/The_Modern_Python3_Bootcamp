#print an emoji using loops
#1 for the first line, 2 for 2nd, etc.
#decided to go further and like yeh idk just mess around
# "Is it worth it? Let me work it
# I put my thing down, flip it and reverse it "

#while loop
i = 0
while i < 11:
	print("\U0001F5FF "*i)
	i += 1

#for loop
for t in range(1,11):
 	print("\U0001F5FF "*(11-t))