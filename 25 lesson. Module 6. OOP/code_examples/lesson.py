# https://tirinox.ru/mro-python/

# class Functor:
#     def __call__(self):
#         print("Hello")

# f = Functor()
# f()
#######################################
# class Functor:
#     def __call__(self, x):
#         if type(x[0]) is int:
#             return self.__merge_sort(x)
#         elif type(x[0]) is float:
#             return self.__bubble_sort(x)
#         else:
#             return self.__quick_sort(x)

#     def __merge_sort(self, x):
#         print("Merge")
#         return x
#     def __bubble_sort(self, x):
#         print("Bubble")
#         return x
#     def __quick_sort(self, x):
#         print("Quick")
#         return x

# class Caller:
#     def __init__(self):
#         self.sort = Functor()
#     def f(self, x):
#         return self.sort(x)

# c = Caller()
# c.f([1,2,3])
# c.f([1.2, 4.6])
# c.f(["sdf",'dgh'])
#####################################################
# class Rectangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w
#     def area(self):
#         return self.l*self.w
#     def perimeter(self):
#         return 2*(self.l+self.w)

# class Square(Rectangle):
#     def __init__(self, l):
#         super().__init__(l,l)

# class Cube(Square):
#     def S(self):
#         return 6 * super(Square, self).area()
#     def V(self):
#         return self.S()*self.l

# class Triangle:
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
#     def area(self):
#         return 0.5 * self.b * self.h
#     def perimeter(self):
#         return self.b + self.h +(self.b**2+self.h**2)**0.5

# class Pyramid(Triangle, Square):
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
#     def area(self):
#         _area = super().area()
#         _perimeter = super().perimeter()
#         return 0.5 * _perimeter * self.h + _area

# # c = Cube(4)
# # print(c.S())
# # print(c.V())

# p = Pyramid(3,2)
# print(p.area())
# print(Pyramid.__mro__)
class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(B, A):
    pass


class E(C, D):
    pass


print(E.__mro__)

##########################################################
# class MyContainer:
#     def __init__(self):
#         self.data = {}
#     def __setitem__(self, key, value):
#         self.data[key] = value
#     def __getitem__(self, key):
#         return self.data[key]

# arr = MyContainer()

# arr[0] = "вода"
# print(arr["water1"])
##########################################################
# arr = [0,4]
# arr[5]
# Создать класс-контейнер на основе списка.
# arr[5]
# При попытке обратиться к несуществующей ячейки
# эта ячейка создаются с каким-то дефолтным значением
# arr[5] = 4556
# В список положится это число.
# class MyContainer:
#     def __init__(self):
#          self.data = []
#     def __setitem__(self, key, value):
#         try:
#             self.data[key] = value
#         except:
#             for _ in range(len(self.data),key):
#                 self.data.append(0)
#             self.data.append(value)

#     def __getitem__(self, key):
#         try:
#             return self.data[key]
#         except:
#             for _ in range(len(self.data),key+1):
#                 self.data.append(0)
#             return self.data[key]

# arr = MyContainer()

# arr[3] = 8

# arr[3]=7
# arr[2] = 4

# print(arr[3])

# print(arr)
#############################################
# class F:
#     pass
# x = F()
# print(type(x))
# print(type(F))
# print(type(type(F)))
################################################3
# for t in int, list, float:
#     print(type(t))
########################################
# F = type('F', (), {})

# x = F()
# print(type(x))
#####################################
# class F:
#     pass

# G = type("G", (F,), dict(attr=100))

# g = G()
# print(g.attr)
# g.attr = 4
# print(g.attr)
# g1 = G()
# print(g1.attr)

# print(g.__class__.__bases__)
########################################
# def foo(self):
#     print(self.x)

# F = type("F",(), {
#     "x": 3,
#     "foo": foo
#     # "foo": lambda self: print(self.x)
# })

# f = F()
# f.foo()
###############################################
# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls, "data"):
#             cls.data = super().__new__(cls)
#         return cls.data


# s = Singleton()
# print(s)
# s1 = Singleton()
# print(s1)
###############################################

# class F:
#     pass


# def new(cls):
#     x = object.__new__(cls)
#     x.attr = 100
#     return x

# F.__new__ = new
# f = F()
# print(f.attr)
################################################
# def new(cls):
#     x = object.__new__(cls)
#     x.attr = 100
#     return x

# type.__new__ = new
##################################
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         x = super().__new__(cls, name, bases, dct)
#         x.attr = 100
#         return x


# class F(metaclass=Meta):
#     pass


# print(F.attr)


# class F1(metaclass=Meta):
#     pass


# print(F1.attr)
###################################3
import sqlite3
class MetaSingleton(type):
    _data = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._data:
            cls._data[cls] = super().__call__(*args, **kwargs)
        return cls._data[cls]
    
class Database(metaclass = MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("data.db")
            self.cursor = self.connection.cursor()
        return self.cursor

db1 = Database().connect()
db2 = Database().connect()
print(db1, db2)
