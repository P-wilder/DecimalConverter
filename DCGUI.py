import tkinter as tk
from DecimalConverter import DecimalConverter as DC

class CalculatorGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("450x600") 
        self.root.title("Decimal Converter")
        self.entry = tk.Entry(self.root, font=("Arial", 32))
        self.entry.pack()
        self.buttonframe = tk.Frame(self.root)
        self.addButtons()
        self.numberstr = ''
        
        self.root.mainloop()
        
    def addNumber(self, value):
        if self.numberstr != '':
            self.entry.delete(0, "end")
        self.numberstr += value
        self.entry.insert(0, self.numberstr)
        
    def clear(self):
        self.numberstr = ''
        self.entry.delete(0, "end")
        
    def add1(self):
        self.addNumber('1')
    
    def add2(self):
        self.addNumber('2')
    
    def add3(self):
        self.addNumber('3')
    
    def add4(self):
        self.addNumber('4')
        
    def add5(self):
        self.addNumber('5')
        
    def add6(self):
        self.addNumber('6')
        
    def add7(self):
        self.addNumber('7')
        
    def add8(self):
        self.addNumber('8')
        
    def add9(self):
        self.addNumber('9')
        
    def addA(self):
        self.addNumber('A')
        
    def addB(self):
        self.addNumber('B')
        
    def addC(self):
        self.addNumber('C')
        
    def addD(self):
        self.addNumber('D')
        
    def addE(self):
        self.addNumber('E')
        
    def addF(self):
        self.addNumber('F')
    
    def add0(self):
        self.addNumber('0')
    
    def addButtons(self):
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.columnconfigure(4, weight=1)
        
        btn1 = tk.Button(self.buttonframe, text="1", font=('Arial', 16), command=self.add1)
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        btn2 = tk.Button(self.buttonframe, text="2", font=('Arial', 16), command=self.add2)
        btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
        btn3 = tk.Button(self.buttonframe, text="3", font=('Arial', 16), command=self.add3)
        btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
        btn4 = tk.Button(self.buttonframe, text="4", font=('Arial', 16), command=self.add4)
        btn4.grid(row=0, column=3, sticky=tk.W+tk.E)
        btn5 = tk.Button(self.buttonframe, text="5", font=('Arial', 16), command=self.add5)
        btn5.grid(row=1, column=0, sticky=tk.W+tk.E)
        btn6 = tk.Button(self.buttonframe, text="6", font=('Arial', 16), command=self.add6)
        btn6.grid(row=1, column=1, sticky=tk.W+tk.E)
        btn7 = tk.Button(self.buttonframe, text="7", font=('Arial', 16), command=self.add7)
        btn7.grid(row=1, column=2, sticky=tk.W+tk.E)
        btn8 = tk.Button(self.buttonframe, text="8", font=('Arial', 16), command=self.add8)
        btn8.grid(row=1, column=3, sticky=tk.W+tk.E)
        btn9 = tk.Button(self.buttonframe, text="9", font=('Arial', 16), command=self.add9)
        btn9.grid(row=2, column=0, sticky=tk.W+tk.E)
        btnA = tk.Button(self.buttonframe, text="A", font=('Arial', 16), command=self.addA)
        btnA.grid(row=2, column=1, sticky=tk.W+tk.E)
        btnB = tk.Button(self.buttonframe, text="B", font=('Arial', 16), command=self.addB)
        btnB.grid(row=2, column=2, sticky=tk.W+tk.E)
        btnC = tk.Button(self.buttonframe, text="C", font=('Arial', 16), command=self.addC)
        btnC.grid(row=2, column=3, sticky=tk.W+tk.E)
        btnD = tk.Button(self.buttonframe, text="D", font=('Arial', 16), command=self.addD)
        btnD.grid(row=3, column=0, sticky=tk.W+tk.E)
        btnE = tk.Button(self.buttonframe, text="E", font=('Arial', 16), command=self.addE)
        btnE.grid(row=3, column=1, sticky=tk.W+tk.E)
        btnF = tk.Button(self.buttonframe, text="F", font=('Arial', 16), command=self.addF)
        btnF.grid(row=3, column=2, sticky=tk.W+tk.E)
        btn0 = tk.Button(self.buttonframe, text="0", font=('Arial', 16), command=self.add0)
        btn0.grid(row=3, column=3, sticky=tk.W+tk.E)
        btnAdd = tk.Button(self.buttonframe, text="+", font=('Arial', 16))
        btnAdd.grid(row=0, column=4, sticky=tk.W+tk.E)
        btnSub = tk.Button(self.buttonframe, text="-", font=('Arial', 16))
        btnSub.grid(row=1, column=4, sticky=tk.W+tk.E)
        btnMult = tk.Button(self.buttonframe, text="*", font=('Arial', 16))
        btnMult.grid(row=2, column=4, sticky=tk.W+tk.E)
        btnDiv = tk.Button(self.buttonframe, text="/", font=('Arial', 16))
        btnDiv.grid(row=3, column=4, sticky=tk.W+tk.E)
        btnDeci = tk.Button(self.buttonframe, text="Decimal", font=('Arial', 16))
        btnDeci.grid(row=4, column=0, sticky=tk.W+tk.E)
        btnBinary = tk.Button(self.buttonframe, text="Binary", font=('Arial', 16))
        btnBinary.grid(row=4, column=1, sticky=tk.W+tk.E)
        btnOct = tk.Button(self.buttonframe, text="Octal", font=('Arial', 16))
        btnOct.grid(row=4, column=2, sticky=tk.W+tk.E)
        btnHex = tk.Button(self.buttonframe, text="Hexadecimal", font=('Arial', 16))
        btnHex.grid(row=4, column=3, sticky=tk.W+tk.E)
        btnClear = tk.Button(self.buttonframe, text="Clear", font=("Arial", 16), command=self.clear)
        btnClear.grid(row=5, column=0, sticky=tk.W+tk.E)
        btnEqual = tk.Button(self.buttonframe, text="=", font=('Arial', 16))
        btnEqual.grid(row=4, column=4, sticky=tk.W+tk.E)
        self.buttonframe.pack(fill='both')
        

if __name__ == "__main__":
    CalculatorGUI()