from tkinter import Tk, Entry,Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357x600+0+0")
        master.configure(background="light blue")
        master.resizable(width=False, height=False)

        self.equation=StringVar()
        self.entry_value=' '
        Entry(width=17,bg='#fff',font=('arial',28,'bold'),textvariable=self.equation,).place(x=0,y=0)

        Button(width=10, height=2, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=10, height=2, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=10, height=2, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=10, height=2, text='C', relief='flat', bg='white', command=self.clear).place(x=270, y=50)
        
        Button(width=10, height=2, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0, y=120)
        Button(width=10, height=2, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90, y=120)
        Button(width=10, height=2, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180, y=120)
        Button(width=10, height=2, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=120)
        
        Button(width=10, height=2, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0, y=190)
        Button(width=10, height=2, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90, y=190)
        Button(width=10, height=2, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180, y=190)
        Button(width=10, height=2, text='*', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=190)
        
        Button(width=10, height=2, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0, y=260)
        Button(width=10, height=2, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90, y=260)
        Button(width=10, height=2, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180, y=260)
        Button(width=10, height=2, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=260)
        
        Button(width=10, height=2, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=0, y=330)
        Button(width=10, height=2, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=90, y=330)
        Button(width=10, height=2, text='=', relief='flat', bg='lightgray', command=self.solve).place(x=180, y=330)
        Button(width=10, height=2, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=330)




    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)    

root = Tk()
calc = Calculator(root)
root.mainloop()