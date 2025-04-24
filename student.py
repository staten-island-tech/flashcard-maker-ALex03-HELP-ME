import json

try:
    with open("hi.json", "r") as file:
        to_dict = json.load(file)
except FileNotFoundError:
    to_dict = []

for i , d in to_dict.items():
    input(i)