# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#     def __eq__(self, second):
#         return self.__x == second.__x and self.__y == second.__y
#     def __ne__(self, second):
#         return not self == second
#     def __gt__(self, second):
#         return True
# a = Point(2,3)
# b = Point(2,3)
# print(a!=b)
# print(a>b)


# class Distance:
#     def __init__(self, m, cm):
#         self.m = m
#         self.cm = cm
#     def __add__(self, second):
#         return Distance(self.m + second.m, self.cm + second.cm)

# d_1 = Distance(2,30)
# d_2 = Distance(3,40)
# d_3 = d_1 + d_2
# print(d_3.m, d_3.cm)
####################################################
#Реализовать Класс комплексных чисел. __init__, __str__, __add__, __eq__, __mul__

class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)


    def __neg__(self):  
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.real} + {self.imag} i"

    def __repr__(self):
        return 'Complex' + str(self)
    
c = Complex(2,3)
d = Complex(5,7)
x = d+c