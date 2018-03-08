# Declare a variable called full_name  that is equal to artist's first  and last  names with a space 
# between. You must reference the values associated with those keys in the artist dictionary.

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)