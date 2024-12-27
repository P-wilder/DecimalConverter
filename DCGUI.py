import tkinter as tk

root = tk.Tk()

root.geometry("800x600") 
root.title("Decimal Converter")

textbox = tk.Text(root, font=("Arial", 14), height=1, width=25)
textbox.pack()

input = tk.Entry(root)
input.pack()

root.mainloop()