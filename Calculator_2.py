from tkinter import Tk, Entry, Button, StringVar, Frame

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("360x600")
        master.configure(background="light blue")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        # Entry widget
        entry = Entry(master, font=('Arial', 24), textvariable=self.equation, bd=10, relief='flat', justify='right')
        entry.pack(fill='both', padx=10, pady=10)

        # Frame for buttons
        button_frame = Frame(master, bg="light blue")
        button_frame.pack()

        # Button layout
        buttons = [
            ['(', ')', '%', 'C'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, char in enumerate(row):
                if char == '=':
                    btn = Button(button_frame, text=char, bg='lightgray', font=('Arial', 18), width=5, height=2,
                                 command=self.solve)
                elif char == 'C':
                    btn = Button(button_frame, text=char, bg='tomato', fg='white', font=('Arial', 18), width=5, height=2,
                                 command=self.clear)
                else:
                    btn = Button(button_frame, text=char, bg='white', font=('Arial', 18), width=5, height=2,
                                 command=lambda ch=char: self.show(ch))
                btn.grid(row=row_index, column=col_index, padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calc = Calculator(root)
root.mainloop()
