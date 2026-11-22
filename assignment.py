import tkinter as tk
from tkinter import messagebox

# Sample Quiz Data: List of question dictionaries
QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 1  # Index of correct answer ('def')
    },
    {
        "question": "What is the correct way to start a 'for' loop in Python?",
        "options": ["For x in range(1, 5)", "for x in range(1, 6)", "for x = 1 to 5", "foreach x in range(5)"],
        "answer": 1
    },
    {
        "question": "Which data structure is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": 2
    },
    {
        "question": "What does CBT stand for?",
        "options": ["Computer-Based Testing", "Central Business Terminal", "Code-Based Technology", "Control Block Task"],
        "answer": 0
    }
]

# Quiz Settings
TOTAL_TIME_SECONDS = 120  # 2 minutes countdown timer


class CBTApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("CBT Examination System")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # State Variables
        self.current_q_index = 0
        self.user_answers = {}  # {question_index: selected_option_index}
        self.time_left = TOTAL_TIME_SECONDS
        self.timer_running = False

        # GUI Setup
        self.setup_ui()

    def setup_ui(self):
        # Header / Timer Bar
        self.top_frame = tk.Frame(self.root, bg="#2C3E50")
        self.top_frame.pack(fill="x")

        self.lbl_title = tk.Label(
            self.top_frame, text="CBT Assessment", font=("Helvetica", 14, "bold"), fg="white", bg="#2C3E50"
        )
        self.lbl_title.pack(side="left", padx=10)

        self.lbl_timer = tk.Label(
            self.top_frame, text="Time Left: 02:00", font=("Helvetica", 12, "bold"), fg="#E74C3C", bg="#2C3E50"
        )
        self.lbl_timer.pack(side="right", padx=10)

        # Question Frame
        self.content_frame = tk.Frame(self.root, padx=20, pady=20)
        self.content_frame.pack(fill="both", expand=True)

        self.lbl_question_no = tk.Label(self.content_frame, text="", font=("Helvetica", 11, "bold"), anchor="w")
        self.lbl_question_no.pack(fill="x", pady=(0, 5))

        self.lbl_question_text = tk.Label(
            self.content_frame, text="", font=("Helvetica", 12), wraplength=540, justify="left", anchor="w"
        )
        self.lbl_question_text.pack(fill="x", pady=(0, 15))

        # Radio Buttons for Options
        self.selected_var = tk.IntVar(value=-1)
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.content_frame,
                text="",
                value=i,
                variable=self.selected_var,
                font=("Helvetica", 11),
                anchor="w",
                command=self.record_answer
            )
            rb.pack(fill="x", pady=4)
            self.option_buttons.append(rb)

        # Bottom Navigation Controls
        self.nav_frame = tk.Frame(self.root, padx=20, pady=15)
        self.nav_frame.pack(fill="x")

        self.btn_prev = tk.Button(self.nav_frame, text="Previous", width=10, command=self.prev_question)
        self.btn_prev.pack(side="left", padx=5)

        self.btn_next = tk.Button(self.nav_frame, text="Next", width=10, command=self.next_question)
        self.btn_next.pack(side="left", padx=5)

        self.btn_submit = tk.Button(
            self.nav_frame, text="Submit Exam", width=12, bg="#27AE60", fg="white", font=("Helvetica", 10, "bold"), command=self.confirm_submit
        )
        self.btn_submit.pack(side="right", padx=5)

        # Start Test
        self.start_timer()
        self.load_question()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if not self.timer_running:
            return

        mins, secs = divmod(self.time_left, 60)
        self.lbl_timer.config(text=f"Time Left: {mins:02d}:{secs:02d}")

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showwarning("Time Up!", "Your time has expired. The test will now submit automatically.")
            self.submit_exam()

    def load_question(self):
        qdata = QUESTIONS[self.current_q_index]

        # Update labels
        self.lbl_question_no.config(text=f"Question {self.current_q_index + 1} of {len(QUESTIONS)}")
        self.lbl_question_text.config(text=qdata["question"])

        # Update options
        for i, option_text in enumerate(qdata["options"]):
            self.option_buttons[i].config(text=option_text)

        # Restore previously selected answer if available
        saved_ans = self.user_answers.get(self.current_q_index, -1)
        self.selected_var.set(saved_ans)

        # Navigation state updates
        self.btn_prev.config(state="disabled" if self.current_q_index == 0 else "normal")
        self.btn_next.config(state="disabled" if self.current_q_index == len(QUESTIONS) - 1 else "normal")

    def record_answer(self):
        self.user_answers[self.current_q_index] = self.selected_var.get()

    def next_question(self):
        if self.current_q_index < len(QUESTIONS) - 1:
            self.current_q_index += 1
            self.load_question()

    def prev_question(self):
        if self.current_q_index > 0:
            self.current_q_index -= 1
            self.load_question()

    def confirm_submit(self):
        unanswered = len(QUESTIONS) - len(self.user_answers)
        msg = "Are you sure you want to submit your test?"
        if unanswered > 0:
            msg = f"You have {unanswered} unanswered question(s).\n\n" + msg

        if messagebox.askyesno("Confirm Submission", msg):
            self.submit_exam()

    def submit_exam(self):
        self.timer_running = False

        # Calculate score
        score = 0
        for i, qdata in enumerate(QUESTIONS):
            if self.user_answers.get(i) == qdata["answer"]:
                score += 1

        percentage = (score / len(QUESTIONS)) * 100

        # Show final result screen
        for widget in self.root.winfo_children():
            widget.destroy()

        result_frame = tk.Frame(self.root, padx=30, pady=30)
        result_frame.pack(fill="both", expand=True)

        tk.Label(result_frame, text="Examination Finished", font=("Helvetica", 18, "bold")).pack(pady=10)
        tk.Label(result_frame, text=f"Your Score: {score} / {len(QUESTIONS)}", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(result_frame, text=f"Percentage: {percentage:.1f}%", font=("Helvetica", 14, "bold"), fg="#27AE60" if percentage >= 50 else "#C0392B").pack(pady=5)

        tk.Button(result_frame, text="Close Application", width=15, command=self.root.destroy).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = CBTApplication(root)
    root.mainloop()