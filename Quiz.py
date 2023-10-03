import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Madrid", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question":"which is capital of telangana?",
                "options": ["hyderabad","varangal","sikindrabad","karimnagar"],
                "correct_answer":"hyderabad"
            },
            # Add more questions here...
        ]

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack()

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack()
        self.next_button.config(state=tk.DISABLED)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)

            self.feedback_label.config(text="")
            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_final_score()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        selected_answer = question_data["options"][selected_option]

        if selected_answer == question_data["correct_answer"]:
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect. The correct answer is {question_data['correct_answer']}."

        self.feedback_label.config(text=feedback)
        self.next_button.config(state=tk.NORMAL)

        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_final_score(self):
        self.question_label.config(text=f"Quiz Completed!\nYour score: {self.score}/{len(self.questions)}")
        self.feedback_label.config(text="")
        self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
