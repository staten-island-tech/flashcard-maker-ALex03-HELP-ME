import json


class card:
    def __init__(self, question, answer):
        self.enter = question

        self.enter1 = answer

    def display_info(self):
        return f"{self.enter} {self.enter1}"
    
    def to_dict(info):
        return {"question": info.enter, "answer": info.enter1}


x =input("what is the question?") 

y= input("What is the answer?")

newCard = card(x,y)
print(newCard.display_info)

with open("hi.json", "w") as json_file:
    json.dump(class, json_file, indent=4)
