import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Entry field to display the expression
        self.input_frame = tk.Frame(self.root, bd=10, relief=tk.RAISED)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(self.input_frame, font=('Arial', 18, 'bold'), textvariable=self.input_text, width=25, bd=5, insertwidth=4, bg="#eee", justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack()

        # Frame for buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        # First row
        self.clear_button = tk.Button(self.buttons_frame, text="C", width=32, height=3, command=self.clear_input)
        self.clear_button.grid(row=0, column=0, columnspan=3)

        self.divide_button = tk.Button(self.buttons_frame, text="/", width=10, height=3, command=lambda: self.update_expression("/"))
        self.divide_button.grid(row=0, column=3)

        # Second row
        self.seven_button = tk.Button(self.buttons_frame, text="7", width=10, height=3, command=lambda: self.update_expression("7"))
        self.seven_button.grid(row=1, column=0)

        self.eight_button = tk.Button(self.buttons_frame, text="8", width=10, height=3, command=lambda: self.update_expression("8"))
        self.eight_button.grid(row=1, column=1)

        self.nine_button = tk.Button(self.buttons_frame, text="9", width=10, height=3, command=lambda: self.update_expression("9"))
        self.nine_button.grid(row=1, column=2)

        self.multiply_button = tk.Button(self.buttons_frame, text="*", width=10, height=3, command=lambda: self.update_expression("*"))
        self.multiply_button.grid(row=1, column=3)

        # Third row
        self.four_button = tk.Button(self.buttons_frame, text="4", width=10, height=3, command=lambda: self.update_expression("4"))
        self.four_button.grid(row=2, column=0)

        self.five_button = tk.Button(self.buttons_frame, text="5", width=10, height=3, command=lambda: self.update_expression("5"))
        self.five_button.grid(row=2, column=1)

        self.six_button = tk.Button(self.buttons_frame, text="6", width=10, height=3, command=lambda: self.update_expression("6"))
        self.six_button.grid(row=2, column=2)

        self.subtract_button = tk.Button(self.buttons_frame, text="-", width=10, height=3, command=lambda: self.update_expression("-"))
        self.subtract_button.grid(row=2, column=3)

        # Fourth row
        self.one_button = tk.Button(self.buttons_frame, text="1", width=10, height=3, command=lambda: self.update_expression("1"))
        self.one_button.grid(row=3, column=0)

        self.two_button = tk.Button(self.buttons_frame, text="2", width=10, height=3, command=lambda: self.update_expression("2"))
        self.two_button.grid(row=3, column=1)

        self.three_button = tk.Button(self.buttons_frame, text="3", width=10, height=3, command=lambda: self.update_expression("3"))
        self.three_button.grid(row=3, column=2)

        self.add_button = tk.Button(self.buttons_frame, text="+", width=10, height=3, command=lambda: self.update_expression("+"))
        self.add_button.grid(row=3, column=3)

        # Fifth row
        self.zero_button = tk.Button(self.buttons_frame, text="0", width=21, height=3, command=lambda: self.update_expression("0"))
        self.zero_button.grid(row=4, column=0, columnspan=2)

        self.decimal_button = tk.Button(self.buttons_frame, text=".", width=10, height=3, command=lambda: self.update_expression("."))
        self.decimal_button.grid(row=4, column=2)

        self.equal_button = tk.Button(self.buttons_frame, text="=", width=10, height=3, command=self.calculate_result)
        self.equal_button.grid(row=4, column=3)

    def update_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set("")

    def calculate_result(self):
        try:
            result = str(eval(self.expression))  # Evaluate the expression
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
