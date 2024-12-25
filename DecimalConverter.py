class DecimalConverter:
        def __init__(self):
                self.deci = None
                self.binary = None
                self.octal = None
                self.hex = None
                
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
                if self.deci == None or value == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToBinary(self.deci)
                else:
                        decimal = value
                        binarylist = []
                        decimal
                        while decimal > 0:
                                binarylist.insert(0, decimal%2)
                                decimal = decimal//2
                        strbinary = ''
                        for i in binarylist:
                                strbinary += str(i)
                        self.binary = strbinary
                        
        def convertToOctal(self, value):
                if self.deci == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToOctal(self.deci)
                else:
                        decimal = value
                        octallist = []
                        decimaltodivide = decimal
                        while decimaltodivide > 0:
                                octallist.insert(0, decimaltodivide%8)
                                decimaltodivide = decimaltodivide//8
                        stroctal= ''
                        for i in octallist:
                                stroctal += str(i)
                        self.octal = stroctal
        
        def convertToHex(self, value):
                if self.deci == None:
                        self.deci = int(input("Please enter decimal value: "))
                        self.convertToHex(self.deci)
                else:
                        decimal = value
                        hexlist = []
                        decimaltodivide = decimal
                        while decimaltodivide > 0:
                                if decimaltodivide % 16 > 9:
                                        match decimaltodivide % 16:
                                                case 10:
                                                        hexlist.insert(0, 'A')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 11:
                                                        hexlist.insert(0, 'B')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 12:
                                                        hexlist.insert(0, 'C')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 13:
                                                        hexlist.insert(0, 'D')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 14:
                                                        hexlist.insert(0, 'E')
                                                        decimaltodivide = decimaltodivide // 16
                                                case 15:
                                                        hexlist.insert(0, 'F')
                                                        decimaltodivide = decimaltodivide // 16
                                else:
                                        hexlist.insert(0, decimaltodivide%16)
                                        decimaltodivide = decimaltodivide // 16
                        strhex= ''
                        for i in hexlist:
                                strhex += str(i)
                        self.hex = strhex
                        
        def addDeci(self, value=0):
                self.deci += value
                self.input(self.deci)
        
        def multiDeci(self, value=1):
                self.deci *= value
                self.input(self.deci)
                
        def subDeci(self, value=0):
                self.deci-= value
                self.input(self.deci)
                
        def divDeci(self, value=1):
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
        DC.input(500)
        print(DC)
        DC.multiDeci(20)
        print(DC)
