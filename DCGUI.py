import tkinter as tk
from DecimalConverter import DecimalConverter as DC

root = tk.Tk()

root.geometry("300x500") 
root.title("Decimal Converter")

textbox = tk.Text(root, font=("Arial", 14), height=1, width=25)
textbox.pack()

input = tk.Entry(root)
input.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 16))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 16))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 16))
btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 16))
btn5.grid(row=1, column=0, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 16))
btn6.grid(row=1, column=1, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="7", font=('Arial', 16))
btn7.grid(row=1, column=2, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonframe, text="8", font=('Arial', 16))
btn8.grid(row=1, column=3, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonframe, text="9", font=('Arial', 16))
btn9.grid(row=2, column=0, sticky=tk.W+tk.E)

btn10 = tk.Button(buttonframe, text="A", font=('Arial', 16))
btn10.grid(row=2, column=1, sticky=tk.W+tk.E)

btn11 = tk.Button(buttonframe, text="B", font=('Arial', 16))
btn11.grid(row=2, column=2, sticky=tk.W+tk.E)

btn12 = tk.Button(buttonframe, text="C", font=('Arial', 16))
btn12.grid(row=2, column=3, sticky=tk.W+tk.E)

btn13 = tk.Button(buttonframe, text="D", font=('Arial', 16))
btn13.grid(row=3, column=0, sticky=tk.W+tk.E)

btn14 = tk.Button(buttonframe, text="E", font=('Arial', 16))
btn14.grid(row=3, column=1, sticky=tk.W+tk.E)

btn15 = tk.Button(buttonframe, text="F", font=('Arial', 16))
btn15.grid(row=3, column=2, sticky=tk.W+tk.E)

btn16 = tk.Button(buttonframe, text="0", font=('Arial', 16))
btn16.grid(row=3, column=3, sticky=tk.W+tk.E)

btn17 = tk.Button(buttonframe, text="+", font=('Arial', 16))
btn17.grid(row=0, column=4, sticky=tk.W+tk.E)

btn18 = tk.Button(buttonframe, text="-", font=('Arial', 16))
btn18.grid(row=1, column=4, sticky=tk.W+tk.E)

btn19 = tk.Button(buttonframe, text="X", font=('Arial', 16))
btn19.grid(row=2, column=4, sticky=tk.W+tk.E)

btn20 = tk.Button(buttonframe, text="/", font=('Arial', 16))
btn20.grid(row=3, column=4, sticky=tk.W+tk.E)

buttonframe.pack(fill='both')

tk.Checkbutton

root.mainloop()