from tkinter import *

def SumDigits(n):
    if n == 0:
        return 0
    return n%10 + SumDigits(n // 10)

def SuperDigit(n):
    if (n//10) == 0:
        return n
    else:
        S = SumDigits(n)
        return SuperDigit(S)


def SumDigitsShow():
    Abox.delete(0, END)
    n = int(E1.get())
    Abox.insert(END, str(SumDigits(n)))

def SuperDigitShow():
    Abox.delete(0, END)
    n = int(E1.get())
    Abox.insert(END, str(SuperDigit(n)))
    

def clear():
    E1.delete(0, END)
    Abox.delete(0, END)
    E1.focus()


root = Tk()

L1 = Label(root, text='Digit Sum and Super Digit Generator', fg='blue')
L2 = Label(root, text='Enter Number:')
E1 = Entry(root, bg='white')
B1 = Button(root, text='Digit Sum', bg='yellow', command=SumDigitsShow)
B2 = Button(root, text='Super Digit', bg='yellow', command=SuperDigitShow)
Abox = Listbox(root, bg='white')
B3 = Button(root, text='Clear', bg='red', command=clear)

L1.pack(anchor=N)
L2.pack(anchor=W)
E1.pack(anchor=W)
B1.pack(anchor=W)
B2.pack(anchor=W)
Abox.pack()
B3.pack()
E1.focus()

root.mainloop()
