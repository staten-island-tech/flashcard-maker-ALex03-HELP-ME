import json


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

class card:
    def __init__(self, question, answer):
        self.enter = question

        self.enter1 = answer

    def display_info(self):
        return f"{self.enter} {self.enter1}"
    
    def to_dict(self):
        return {"question": self.enter, "answer": self.enter1}


x =input("what is the question?") 

y= input("What is the answer?")

newCard = card(x,y)
print(newCard.display_info)

with open("hi.json", "w") as json_file:
    json.dump(newCard. to_dict(), json_file, indent=4)

