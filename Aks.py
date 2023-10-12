import tkinter as tk

# Define the questions
questions = ["How much do you like cereal?", "How much do you like oatmeal?"]
question_counter = 0  # Initialize the question counter

def submit_answer():
    global question_counter
    user_answer = scale.get()
    print(f"User's answer for '{questions[question_counter]}': {user_answer}")

    # Move to the next question or close the window if all questions are answered
    question_counter += 1
    if question_counter < len(questions):
        question_label.config(text=questions[question_counter])
        scale.set(1)  # Reset the scale to the initial value
    else:
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Interactive Box")

# Create a label for the question
question_label = tk.Label(root, text=questions[question_counter])
question_label.pack()

# Create a scale widget with values from 1 to 10
scale = tk.Scale(root, from_=1, to=10, orient="horizontal")
scale.pack()

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack()

# Start the main event loop
root.mainloop()
