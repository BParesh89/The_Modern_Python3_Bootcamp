# Using a nested list comprehension and range(), create a variable called answer  
# with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .

answer = [ [val for val in range(0,3)] for i in range(0,3)]
print(answer)