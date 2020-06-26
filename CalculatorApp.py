from tkinter import *
from ConsoleCalculator import *

# PLEASE ENSURE YOU HAVE ConsoleCalculator.py AVAILABLE FOR THIS APPLICATION OR THIS WILL NOT WORK:
# https://github.com/marcusvongsykeo/portfolio/blob/master/ConsoleCalculator.py

formula = ""
ans = ""
root = Tk()
root.title("Calculator")

# Define formula field (e) and answer field
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=1, pady=20)

answer = Entry(root, width=30, borderwidth=5)
answer.grid(row=1, column=1, columnspan=2, padx=0, pady=1)

answer_label = Label(root, text="Ans:")
answer_label.grid(row=1, column=0)


def button_click(number):
    global formula
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    formula = e.get()
    return

def evaluate():
    global formula
    formula = e.get()
    global ans
    answer.delete(0, END)
    result = str(calculate(formula))
    ans = result
    answer.insert(0, result)
    e.delete(0, END)


# Define Buttons
button_width = 40
button_height = 20
button_1 = Button(root, text="1", padx=button_width, pady=button_height, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=button_width, pady=button_height, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=button_width, pady=button_height, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=button_width, pady=button_height, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=button_width, pady=button_height, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=button_width, pady=button_height, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=button_width, pady=button_height, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=button_width, pady=button_height, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=button_width, pady=button_height, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=button_width, pady=button_height, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=button_width, pady=button_height, command=lambda: button_click('+'))
button_sub = Button(root, text="-", padx=button_width+1, pady=button_height, command=lambda: button_click('-'))
button_mult = Button(root, text="×", padx=button_width, pady=button_height, command=lambda: button_click('*'))
button_div = Button(root, text="÷", padx=button_width, pady=button_height, command=lambda: button_click('/'))
button_pow = Button(root, text="^", padx=button_width-1, pady=button_height, command=lambda: button_click('^'))
button_dot = Button(root, text=".", padx=button_width+1, pady=button_height, command=lambda: button_click('.'))
button_ans = Button(root, text="Ans", padx=button_width-7, pady=button_height, command=lambda: button_click(ans))
button_ob = Button(root, text="(", padx=button_width+1, pady=button_height, command=lambda: button_click('('))
button_cb = Button(root, text=")", padx=button_width+1, pady=button_height, command=lambda: button_click(')'))
button_equal = Button(root, text="=", padx=button_width, pady=button_height, command=evaluate)
button_clear = Button(root, text="Clr", padx=button_width-4, pady=button_height, command=lambda: e.delete(0, END))



# Put buttons on screen
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_ans.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_dot.grid(row=6, column=2)

button_clear.grid(row=1, column=3, columnspan=1)


button_ob.grid(row=2, column=0)
button_cb.grid(row=2, column=1)
button_pow.grid(row=2, column=2)

button_div.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_sub.grid(row=4, column=3)
button_add.grid(row=5, column=3)
button_equal.grid(row=6, column=3)

root.mainloop()
