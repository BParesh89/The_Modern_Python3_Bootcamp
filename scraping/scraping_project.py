# create a quote guessing game
# use quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice, shuffle


def extract_quotes():
    main_url = "http://quotes.toscrape.com"
    page_url = ""
    all_quotes = []

    while True:
        # accessing the website and getting the html
        sleep(1)
        response = requests.get(main_url+page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        # extracting the quote data from the html
        for q in quotes:
            text = q.find("span").get_text()
            author = q.find("small").get_text()
            bio = q.find("a")["href"]
            all_quotes.append([text, author, bio])
            # print(all_quotes)

        # extracting the nextpage data
        if soup.find(class_="next"):
            page_url = soup.find(class_="next").contents[1]['href']
        else:
            return all_quotes


def invoke_hint(url, num, name):

    print("Here's a hint:")
    if num == 0:
        # birth date and location
        response = requests.get('http://quotes.toscrape.com'+url)
        soup = BeautifulSoup(response.text, "html.parser")
        birth_span = soup.find_all('span')
        dob = birth_span[0].get_text()
        lob = birth_span[1].get_text()
        print(f'This person was born on {dob} {lob}')

    elif num == 1:
        # initals of name
        name_list = name.split(' ')
        print(f"This person's initals are: {name_list[0][0]} {name_list[1][0]}")
    elif num == 2:
        # jumbled name
        name_chars = list(name.lower())
        shuffle(name_chars)
        print(f"This person's name jumbled is: {''.join(name_chars)}")


def play_again():
    # Play again logic
    again = input('Do you want to play again? (y/n) ')
    while again not in ['y', 'n']:
        again = input('Do you want to play again? (y/n) ')
    if again == 'n':
        return False
    elif again == 'y':
        return True


all_quotes = extract_quotes()

# game part
while True:
    user_quote = choice(all_quotes)
    print(f"-----\n{user_quote[0]}\n-----")
    print('Who said this quote?')
    for i in range(0, 4):
        guess = input(f"you have {4-i} guesses remaining: ")
        if guess == user_quote[1]:
            # when correct
            print("Congratulations, you were correct!")
            break
        elif i not in [0, 1, 2]:
            # if wrong and ran out of guesses
            print(f"The quote was said by {user_quote[1]}")
            break
        else:
            # if wrong and guesses reamin, invoke hint
            invoke_hint(user_quote[2], i, user_quote[1])
    # play again
    again = play_again()
    if not again:
        break
