import json

try:
    with open("hi.json", "r") as file:
        to_dict = json.load(file)
except Exception:
    to_dict = []

class card:
    def __init__(self, question, answer):
        self.enter = question

        self.enter1 = answer

    def display_info(self):
        return f"{self.enter} {self.enter1}"
    
    def to_dict(self):
        return {self.enter: self.enter1}


x =input("what is the question?") 

y= input("What is the answer?")

newCard = card(x,y)
print(newCard.to_dict())
to_dict.append(newCard.to_dict())

with open("hi.json", "w") as json_file:
    json.dump(to_dict, json_file, indent=4)
