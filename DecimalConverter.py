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
                    print("1. Convert from selected base\n2. Add\n3. Multiply\n4. Subtract\n5. Divide\n6. Print")
                    function = input("Please select a function: ")
                if function != '1' and function != '6' and base == '1':
                    value = int(input("Please enter a decimal value: "))
                match base:
                    case '1':
                        match function:
                            case '1':
                                self.input()
                            case '2':
                                self.addDeci(value)
                            case '3':
                                self.multiDeci(value)
                            case '4':
                                self.subDeci(value)
                            case '5':
                                self.divDeci(value)
                            case '6':
                                self.printDeci()
                            case _:
                                print("Please enter a valid choice.")
                    case '2':
                        if function != '6':
                            decimal = self.convertFromBinary()
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
                            case '6':
                                self.printBinary()
                            case _:
                                print("Please enter a valid choice.")
                    case '3':
                        if function != '6':
                            decimal = self.convertFromOctal()
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
                            case '6':
                                self.printOctal()
                            case _:
                                print("Please enter a valid choice.")
                    case '4':
                        if function != '6':
                            decimal = self.convertFromHex()
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
                            case '6':
                                self.printHex()
                            case _:
                                print("Please enter a valid choice.")
                    case '5':
                        self.printAll()
                    case '6':
                        return
                        
if __name__ == "__main__":
        DC = DecimalConverter()
        DC.main()
