#loop through 1-20 inclusive
#if 4 and 13 print "x is unlucky"
#if odd print "x is odd"
#if even print "x is even"

for x in range (1,21):
	print(f"{x} is ",end="")
	if x == 4 or x == 13:
		print("unlucky")
	elif x%2 == 1:
		print("odd")
	else:
		print("even")
