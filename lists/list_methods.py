# Create a list called instructors

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

# Remove the last value in the list

# Remove the first value in the list

# Add the string "Done" to the beginning of the list

# Run the tests to make sure you've done this correctly!

instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])

instructors.pop()
instructors.remove(instructors[0])
instructors.reverse()
instructors.append("Done")
instructors.reverse()

print(instructors)