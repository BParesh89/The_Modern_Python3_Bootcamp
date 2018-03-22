from csv import reader


def print_users():

    with open('users.csv') as file:
        csv_reader = reader(file)
        next(csv_reader)
        for u in csv_reader:
            print(f"{u[0]} {u[1]}")


print_users()
