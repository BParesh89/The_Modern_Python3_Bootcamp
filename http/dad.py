from termcolor import colored
from pyfiglet import figlet_format
import requests


def tell_joke(joke_list):
    from random import choice
    return choice(joke_list)


url = "https://icanhazdadjoke.com/search"

print(colored(figlet_format("DAD JOKEZ!!!"), "magenta"))

joke_topic = input("Give me a topic for a dad joke: ")

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": joke_topic}
)

data = response.json()

jokes = [joke["joke"] for joke in data["results"]]

if not len(data["results"]):
    print(f"Sorry I don't know any jokes about {joke_topic}")
elif len(data["results"]) == 1:
    print(f"I know one joke about {joke_topic}. Here it is:\n{tell_joke(jokes)}")
else:
    print(f"I know {len(jokes)} jokes about {joke_topic}. Here's one:\n{tell_joke(jokes)}")
