import json

try:
    with open("hi.json", "r") as file:
        to_dict = json.load(file)
except FileNotFoundError:
    to_dict = []

# Loop through the list using enumerate to get both the index and the item
for i, d in enumerate(to_dict):
    user_input = input(f"Item {i + 1}: {d} - Please provide your answer: ")
    
    # Assuming you have some logic to verify the user's input, e.g., comparing to a correct answer.
    correct_answer = "correct"  # Replace with your actual logic or value to compare against
    
    if user_input.lower() != correct_answer.lower():
        print("No, that's incorrect.")
    else:
        print(f"You answered: {user_input}")