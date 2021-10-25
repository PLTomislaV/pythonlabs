


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, second_number):
        r = self.real + second_number.real
        i = self.imaginary + second_number.imaginary
        return ComplexNumber(r, i)

    def subtract(self, second_number):
        r = self.real - second_number.real
        i = self.imaginary - second_number.imaginary
        return ComplexNumber(r, i)

    def multiply(self, second_number):
        r = self.real * second_number.real
        i = self.imaginary * second_number.imaginary
        return ComplexNumber(r, i)

    def divide(self, second_number):
        r = self.real / second_number.real
        i = self.imaginary / second_number.imaginary
        return ComplexNumber(r, i)

    def tostr(self):
        if self.imaginary < 0:
            return "{} {}i".format(self.real, self.imaginary)
        else:
            return "{} +{}i".format(self.real, self.imaginary)


print("Try to input equation like: 5 +8i / 10 -9i :")

while True:
    try:
        eq = input().split()
        c1 = ComplexNumber(float(eq[0]), float(eq[1][:len(eq[1])-1]))
        c2 = ComplexNumber(float(eq[3]), float(eq[4][:len(eq[4])-1]))
        operation = eq[2]

        if operation == '/':
            print(c1.divide(c2).tostr())
            break
        elif operation == '*':
            print(c1.multiply(c2).tostr())
            break
        elif operation == '+':
            print(c1.add(c2).tostr())
            break
        elif operation == '-':
            print(c1.subtract(c2).tostr())
            break
        else:
            print("Invalid operation sign. Please try again.")
            print("Try to input equation like: 5 +8i / 10 -9i ")

    except ValueError:
        print('Invalid Input. Try again.')
        print("Try to input equation like: 5 +8i / 10 -9i ")
