import json

try:
    with open("hi.json", "r") as file:
        to_dict = json.load(file)
except FileNotFoundError:
    to_dict = []

# Loop through the list using enumerate to get both the index and the item
for i, d in enumerate(to_dict):
    user_input = input(f"Item {i + 1}: {d} - Please provide your answer: ")
    # You can do something with user_input here if needed
    print(f"You answered: {user_input}")