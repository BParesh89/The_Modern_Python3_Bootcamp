from csv import reader, writer


def update_users(old_first, old_last, new_first, new_last):

    with open('users.csv', "r") as file:
        csv_reader = list(reader(file))
        counter = 0
        for i in range(0, len(csv_reader)):
            if (csv_reader[i][0] == f'{old_first}') & (csv_reader[i][1] == f'{old_last}'):
                csv_reader[i][0] = new_first
                csv_reader[i][1] = new_last
                counter += 1
        with open('users.csv', 'w') as file:
        	csv_writer = writer(file)
        	for user in csv_reader:
        		csv_writer.writerow(user)
    return f"Users updated: {counter}"

print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
print(update_users("Not", "Here", "Still not", "Here"))