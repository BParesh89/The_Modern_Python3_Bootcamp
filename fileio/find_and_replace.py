def find_and_replace(filename, find_word, replacement_word):
    with open(filename, 'r+') as file:
        text = file.read()

        text_words = text.split(find_word)
        text_replaced = f'{replacement_word}'.join(text_words)
        file.seek(0)
        file.write(text_replaced)


find_and_replace("story.txt", "Alice", "Tim")
