from csv import reader, writer


def delete_users(first, last):

    with open('users.csv', "r") as file:
        csv_reader = list(reader(file))
        data = list(csv_reader)

        data = [user for user in data if user != [f'{first}', f'{last}']]
        users_del = len(csv_reader) - len(data)

        with open('users.csv', 'w') as file:
            csv_writer = writer(file)
            for user in data:
                csv_writer.writerow(user)

    return f"Users deleted: {users_del}"


print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))
