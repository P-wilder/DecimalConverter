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
        self.numberstr1 = ''
        self.isNum1Done = False
        self.numberstr2 = ''
        self.result = ''
        self.base1 = 'd'
        self.base2 = 'd'
        self.operator = ''
        
        self.root.mainloop()
        
    def setBase(self, base):
        if self.isNum1Done == False and self.numberstr1 == '':
            if base == 'd':
                self.base1 = 'd'
            elif base == 'b':
                self.base1 = 'b'
            elif base == 'o':
                self.base1 = 'o'
            elif base == 'h':
                self.base1 = 'h'
        elif self.isNum1Done == True and self.numberstr2 == '':
            if base == 'd':
                self.base2 = 'd'
            elif base == 'b':
                self.base2 = 'b'
            elif base == 'o':
                self.base2 = 'o'
            elif base == 'h':
                self.base2 = 'h'
                
        
    def setDecimal(self):
        self.setBase('d')
        
    def setBinary(self):
        self.setBase('b')
        
    def setOctal(self):
        self.setBase('o')
    
    def setHexadecimal(self):
        self.setBase('h')
        
    def setOperator(self, operator):
        if self.isNum1Done == False:
            self.operator = operator
            self.isNum1Done = True
            self.entry.delete(0, 'end')
        
    def setAdd(self):
        self.setOperator('+')
        
    def setSubtract(self):
        self.setOperator('-')
        
    def setMultiply(self):
        self.setOperator('*')
        
    def setDivide(self):
        self.setOperator('/')
        
    def addNumberToString(self, value):
        if self.isNum1Done == False:
            if self.numberstr1 != '' :
                self.entry.delete(0, "end")
            self.numberstr1 += value
            self.entry.insert(0, self.numberstr1)
        else:
            if self.numberstr2 != '':
                self.entry.delete(0, "end")
            self.numberstr2 += value
            self.entry.insert(0, self.numberstr2)
        
    def clear(self):
        self.numberstr1 = ''
        self.numberstr2 = ''
        self.isNum1Done = False
        self.entry.delete(0, "end")
        
    def add1(self):
        self.addNumberToString('1')
    
    def add2(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('2')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('2')
        
    
    def add3(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('3')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('3')
        
    
    def add4(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('4')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('4')
        
        
    def add5(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('5')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('5')
        
        
    def add6(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('6')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('6')
        
        
    def add7(self):
        if self.isNum1Done == False:
            if self.base1 == 'b':
                pass
            else:
                self.addNumberToString('7')
        else:
            if self.base2 == 'b':
                pass
            else:
                self.addNumberToString('7')
        
    def add8(self):
        if self.isNum1Done == False:
            if self.base1 != 'h' and self.base1 != 'd':
                pass
            else:
                self.addNumberToString('8')
        else:
            if self.base2 != 'h' and self.base2 != 'd':
                pass
            else:
                self.addNumberToString('8')
        
    def add9(self):
        if self.isNum1Done == False:
            if self.base1 != 'h' and self.base1 != 'd':
                pass
            else:
                self.addNumberToString('9')
        else:
            if self.base2 != 'h' and self.base2 != 'd':
                pass
            else:
                self.addNumberToString('9')
        
    def addA(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('A')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('A')
        
    def addB(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('B')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('B')
        
    def addC(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('C')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('C')
        
    def addD(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('D')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('D')
        
    def addE(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('E')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('E')
        
    def addF(self):
        if self.isNum1Done == False:
            if self.base1 != 'h':
                pass
            else:
                self.addNumberToString('F')
        else:
            if self.base2 != 'h':
                pass
            else:
                self.addNumberToString('F')
    
    def add0(self):
        self.addNumberToString('0')
    
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
        btnAdd = tk.Button(self.buttonframe, text="+", font=('Arial', 16), command=self.setAdd)
        btnAdd.grid(row=0, column=4, sticky=tk.W+tk.E)
        btnSub = tk.Button(self.buttonframe, text="-", font=('Arial', 16), command=self.setSubtract)
        btnSub.grid(row=1, column=4, sticky=tk.W+tk.E)
        btnMult = tk.Button(self.buttonframe, text="*", font=('Arial', 16), command=self.setMultiply)
        btnMult.grid(row=2, column=4, sticky=tk.W+tk.E)
        btnDiv = tk.Button(self.buttonframe, text="/", font=('Arial', 16), command=self.setDivide)
        btnDiv.grid(row=3, column=4, sticky=tk.W+tk.E)
        btnDeci = tk.Button(self.buttonframe, text="Decimal", font=('Arial', 16), command=self.setDecimal)
        btnDeci.grid(row=4, column=0, sticky=tk.W+tk.E)
        btnBinary = tk.Button(self.buttonframe, text="Binary", font=('Arial', 16), command=self.setBinary)
        btnBinary.grid(row=4, column=1, sticky=tk.W+tk.E)
        btnOct = tk.Button(self.buttonframe, text="Octal", font=('Arial', 16), command=self.setOctal)
        btnOct.grid(row=4, column=2, sticky=tk.W+tk.E)
        btnHex = tk.Button(self.buttonframe, text="Hexadecimal", font=('Arial', 16), command=self.setHexadecimal)
        btnHex.grid(row=4, column=3, sticky=tk.W+tk.E)
        btnClear = tk.Button(self.buttonframe, text="Clear", font=("Arial", 16), command=self.clear)
        btnClear.grid(row=5, column=0, sticky=tk.W+tk.E)
        btnEqual = tk.Button(self.buttonframe, text="=", font=('Arial', 16))
        btnEqual.grid(row=4, column=4, sticky=tk.W+tk.E)
        self.buttonframe.pack(fill='both')
        
if __name__ == "__main__":
    CalculatorGUI()