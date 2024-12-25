class DecimalConverter:
        def __init__(self):
                self.deci = None
                self.binary = None
                self.octal = None
                self.hex = None
                self.binarylist = []
                self.octallist = []
                self.hexlist = []
                
        def __str__(self):
                str = ("Decimal: {}\n".format(self.deci) + "Binary: {}\n".format(self.binary) +
                "Octal: {}\n".format(self.octal) + "Hexadecimal: {}".format(self.hex))
                return str
                
        def input(self, value=None):
                if value == None:
                        self.deci = int(input("Please enter decimal value: "))
                else:
                        self.deci = value
                self.convertToBinary(self.deci)
                self.convertToOctal(self.deci)
                self.convertToHex(self.deci)
                
        def convertToBinary(self, value=None):
                if value == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToBinary(self.deci)
                else:
                        decimal = value
                        decimal
                        self.binarylist.clear()
                        while decimal > 0:
                                self.binarylist.insert(0, decimal%2)
                                decimal = decimal//2
                        strbinary = ''
                        for i in self.binarylist:
                                strbinary += str(i)
                        self.binary = strbinary
                        
        def convertToOctal(self, value=None):
                if value == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToOctal(self.deci)
                else:
                        decimal = value
                        self.octallist.clear()
                        decimaltodivide = decimal
                        while decimaltodivide > 0:
                                self.octallist.insert(0, decimaltodivide%8)
                                decimaltodivide = decimaltodivide//8
                        stroctal= ''
                        for i in self.octallist:
                                stroctal += str(i)
                        self.octal = stroctal
        
        def convertToHex(self, value=None):
                if value == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToHex(self.deci)
                else:
                        decimal = value
                        self.hexlist.clear()
                        decimaltodivide = decimal
                        while decimaltodivide > 0:
                                if decimaltodivide % 16 > 9:
                                        match decimaltodivide % 16:
                                                case 10:
                                                        self.hexlist.insert(0, 'A')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 11:
                                                        self.hexlist.insert(0, 'B')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 12:
                                                        self.hexlist.insert(0, 'C')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 13:
                                                        self.hexlist.insert(0, 'D')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 14:
                                                        self.hexlist.insert(0, 'E')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 15:
                                                        self.hexlist.insert(0, 'F')
                                                        decimaltodivide = decimaltodivide // 16
                                else:
                                        self.hexlist.insert(0, decimaltodivide%16)
                                        decimaltodivide = decimaltodivide // 16
                        strhex= ''
                        for i in self.hexlist:
                                strhex += str(i)
                        self.hex = strhex
                        
        def addDeci(self, value=0):
                print("Adding {a} to {b}".format(a=self.deci, b=value))
                self.deci += value
                self.input(self.deci)
        
        def multiDeci(self, value=1):
                print("Multiplying {a} by {b}".format(a=self.deci, b=value))
                self.deci *= value
                self.input(self.deci)
                
        def subDeci(self, value=0):
                print("Subtracting {a} by {b}".format(a=self.deci, b=value))
                self.deci-= value
                self.input(self.deci)
                
        def divDeci(self, value=1):
                print("Dividing {a} by {b}".format(a=self.deci, b=value))
                self.deci = self.deci / value
                self.input(self.deci)
                        
        def printHex(self):
                print("Hexadecimal: {}".format(self.hex))
                
        def printOctal(self):
                print("Octal: {}".format(self.octal))
                
        def printBinary(self):
                print("Binary: {}".format(self.binary))
        
        def printAll(self):
                print("Decimal: {}".format(self.deci))
                self.printBinary()
                self.printOctal()
                self.printHex()
                        
                        
if __name__ == "__main__":
        DC = DecimalConverter()
        DC.input()
        print(DC)
        DC.multiDeci(20)
        print(DC)
