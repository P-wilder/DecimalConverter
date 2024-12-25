class DecimalConverter:
        def __init__(self):
                self.deci = 0
                self.binary = '0'
                self.octal = '0'
                self.hex = '0'
                
        def __str__(self):
                str = ("Decimal: {}\n".format(self.deci) + "Binary: {}\n".format(self.binary) +
                "Octal: {}\n".format(self.octal) + "Hexadecimal: {}".format(self.hex))
                return str
            
        def setAlltoZero(self):
            self.deci = 0
            self.binary = '0'
            self.octal = '0'
            self.hex = '0'
                
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
                        binarylist = []
                        while decimal > 0:
                                binarylist.insert(0, decimal%2)
                                decimal = decimal//2
                        strbinary = ''
                        for i in binarylist:
                                strbinary += str(i)
                        self.binary = strbinary
                        
        def convertToOctal(self, value=None):
                if value == None:
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
        
        def convertToHex(self, value=None):
                if value == None:
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
                print("Adding {b} to {a}".format(a=self.deci, b=value))
                self.deci += value
                self.input(self.deci)
        
        def multiDeci(self, value=1):
                print("Multiplying {a} by {b}".format(a=self.deci, b=value))
                self.deci *= value
                self.input(self.deci)
                
        def subDeci(self, value=0):
            if self.deci < value:
                self.setAlltoZero()
            else:
                print("Subtracting {a} by {b}".format(a=self.deci, b=value))
                self.deci-= value
                self.input(self.deci)
                
        def divDeci(self, value=1):
                print("Dividing {a} by {b}".format(a=self.deci, b=value))
                self.deci = self.deci / value
                self.input(self.deci)
                
        def convertFromBinary(self, binaryValue=''):
                if binaryValue == '':
                    binaryValue = input("Please enter binary value: ")
                    return self.convertFromBinary(binaryValue)
                else:
                    decimal = 0
                    for i in range(len(binaryValue)):
                        decimal += int(binaryValue[-(i + 1)]) * (2 ** i)
                    return decimal
        
        def convertFromOctal(self, octalValue=''):
            if octalValue == '':
                octalValue = input("Please enter octal value: ")
                return self.convertFromOctal(octalValue)
            else:
                decimal = 0
                for i in range(len(octalValue)):
                    decimal += int(octalValue[-(i + 1)]) * (8 ** i)
                return decimal
            
        def convertFromHex(self, hexValue=''):
            if hexValue == '':
                hexValue = input("Please enter hex value: ")
                return self.convertFromHex(hexValue)
            else:
                decimal = 0
                for i in range(len(hexValue)):
                    match hexValue[-(i + 1)].upper():
                        case 'A':
                            decimal += 10 * (16 ** i)
                        case 'B':
                            decimal += 11 * (16 ** i)
                        case 'C':
                            decimal += 12 * (16 ** i)
                        case 'D':
                            decimal += 13 * (16 ** i)
                        case 'E':
                            decimal += 14 * (16 ** i)
                        case 'F':
                            decimal += 15 * (16 ** i)
                        case _:
                            decimal += int(hexValue[-(i + 1)]) * (16 ** i)
                return decimal
                            
        def printDeci(self):
            print("Decimal: {}".format(self.deci))
                            
        def printHex(self):
                print("Hexadecimal: {}".format(self.hex))
                
        def printOctal(self):
                print("Octal: {}".format(self.octal))
                
        def printBinary(self):
                print("Binary: {}".format(self.binary))
        
        def printAll(self):
                self.printDeci()
                self.printBinary()
                self.printOctal()
                self.printHex()
                
        def main(self):
            base = ''
            function = ''
            value = 0
            while base != '6':
                print("1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n5. Print all\n6. Quit")
                base = input("Please select a base: ")
                if base == '6':
                    return
                if base != '5':
                    print("1. Convert from selected base\n2. Add\n3. Multiply\n4. Subtract\n5. Divide")
                    function = input("Please select a function: ")
                if base == '1':
                    value = input("Please enter a decimal value: ")
                match base:
                    case '1':
                        decimal = int(value)
                    case '2':
                        decimal = self.convertFromBinary()
                    case '3':
                        decimal = self.convertFromOctal()
                    case '4':
                        decimal = self.convertFromHex()
                    case '5':
                        self.printAll()
                    case '6':
                        return
                if base != '5':
                    match function:
                        case '1':
                            self.input(decimal)
                        case '2':
                            self.addDeci(decimal)
                        case '3':
                            self.multiDeci(decimal)
                        case '4':
                            self.subDeci(decimal)
                        case '5':
                            self.divDeci(decimal)
                        case _:
                            print("Please enter a valid choice.")
                        
if __name__ == "__main__":
        DC = DecimalConverter()
        DC.main()
