from csv import reader


def find_user(first, last):

    with open('users.csv') as file:
        csv_reader = list(reader(file))

        for i in range(0, len(csv_reader)):
            if (csv_reader[i][0] == f'{first}') & (csv_reader[i][1] == f'{last}'):
                return i
        return f"{first} {last} not found."


print(find_user("Colt", "Steele"))
print(find_user('x', 'y'))
print(find_user('Alan', 'Turing'))
