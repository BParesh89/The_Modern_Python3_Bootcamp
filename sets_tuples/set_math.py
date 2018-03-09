# just playing around with the | and &

math_students = {'Tim', 'Pepsi', 'Coke', 'Dog', 'Cat', 'Wayne'}
chem_students = {'Jess', 'Kim', 'Pepsi', 'Jeff', 'Michael', 'Jack', 'Dog', "Zelda"}
wood_students = {'Kyle', 'Pepsi', 'Link', 'Zelda', 'Cigarettes', 'Sportsball'}

# print(math_students & chem_students & wood_students)
# print(math_students & chem_students | wood_students)
print(math_students | chem_students & wood_students)
