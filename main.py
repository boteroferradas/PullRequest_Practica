class CalculadoraBinaria:
    def __init__(self, a, b):
        self.setA(a)
        self.setB(b)

    def setA(self, a):
        if isinstance (a, int) or isinstance(a, float) or isinstance(a,complex):
            self.__a = a
            return self.__a
        else:
            raise TypeError("Tipo incorrecto. Só se admiten int, float, complex")

    def setB(self, b):
        if isinstance(b, int) or isinstance(b, float) or isinstance(b, complex):
            self.__b = b
            return self.__b
        else:
            self.__b = 0
            return self.__b

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b

    def operacion(self, op):
        """
        :param op:
        :return:
        :except: ValueError
        """

        if op == '+':
            return self.__a + self.__b
        elif op == '-':
            return self.__a - self.__b
        elif op == '*':
            return self.__a * self.__b
        elif op == '/':
            return self.__a / self.__b
        else:
            raise ValueError("Operador non valiido")

    a = property (getA, setA)
    b = property (getB, setB)

if __name__ == '__main__':
    c1 = CalculadoraBinaria(4, 4)
    c1.a = 1
    print(c1.operacion("+"))
    c2 = CalculadoraBinaria(4, 0)

    try:
        print (c2.operacion('/'))
    except ZeroDivisionError:
        print("Non se pode dividir por cero")
        b = c2.b
        while b == 0:
            b = int(input("Introduze un divisor: "))
        c2.b = b
        print(c2.operacion('/'))