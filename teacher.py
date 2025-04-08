import json

enter = input("what is the question?")

enter1 = input("What is the answer?")


with open("cars.json", "w") as file:
    json.dump(fash_data, file, indent=4)

