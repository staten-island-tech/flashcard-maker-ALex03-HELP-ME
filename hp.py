import json

try:
    with open("hi.json", "r") as file:
        to_dict = json.load(file)
except FileNotFoundError:
    to_dict = []

# Assuming each item in the JSON contains a 'question' and 'answer' field
for i, d in enumerate(to_dict):
    question = d.get("question")
    correct_answer = d.get("answer")

    # Ask the user for an answer
    if question and correct_answer is not None:
        user_input = input(f"Question {i + 1}: {question} - Your answer: ")

        # Check if the answer is correct
        if user_input.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
    else:
        print(f"Item {i + 1} does not have a valid question or answer.")