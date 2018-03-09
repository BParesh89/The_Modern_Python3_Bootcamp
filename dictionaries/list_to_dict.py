person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]:person[i][1] for i in range(0,len(person))}
print(answer)