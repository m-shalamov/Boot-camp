# Python code to illustrate program
# using functors

# class Functor(object):
#     def __init__(self, n=10):
#         self.n = n

#     # This construct allows objects to be called as functions in python
#     def __call__(self, x) :
#         x_first = x[0]
#         if type(x_first) is int:
#             return self. __MergeSort(x)
#         if type(x_first) is float:
#             return self. __HeapSort(x)
#         else :
#             return self.__QuickSort(x)

#     def __MergeSort(self,a):
#         #" Dummy MergeSort "
#         print ("Data is Merge sorted")
#         return a
#     def __HeapSort(self,b):
#         # " Dummy HeapSort "
#         print ("Data is Heap sorted")
#         return b
#     def __QuickSort(self,c):
#         # "Dummy QuickSort"
#         print ("Data is Quick sorted")
#         return c

# Now let's code the class which will call the above functions.
# Without the functor this class should know which specific function to be called
# based on the type of input

### USER CODE
# class Caller(object):
#     def __init__(self):
#         self.sort=Functor()

#     def Dosomething(self,x):
# # Here it simply calls the function and doesn't need to care about
# # which sorting is used. It only knows that sorted output will be the
# # result of this call
#         return self.sort(x)

# Call=Caller()

# # Here passing different input
# print(Call.Dosomething([5,4,6])) # Mergesort

# print(Call.Dosomething([2.23,3.45,5.65])) # heapsort
# print(Call.Dosomething(['a','s','b','q'])) # quick sort
# # creating word vocab
###################################################################
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

# class Cube(Square):
#     def surface_area(self):
#         face_area = super().area()
#         return face_area * 6

#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length

# c = Cube(4)
# print(c.surface_area())
################################################
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# class Square(Rectangle):
#     def __init__(self, length):
#         super(Square, self).__init__(length, length)
# class Cube(Square):
#     def surface_area(self):
#         face_area = super(Square, self).area()
#         return face_area * 6

#     def volume(self):
#         face_area = super(Square, self).area()
#         return face_area * self.length

# c = Cube(4)
# print(c.surface_area())
#################################################
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width


# class Square(Rectangle):
#     def __init__(self, length):
#         super(Square, self).__init__(length, length)


# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# class RightPyramid(Triangle, Square):
#     def __init__(self, base, slant_height):
#         self.base = base
#         self.slant_height = slant_height

#     def area(self):
#         base_area = super().area()
#         perimeter = super().perimeter()
#         return 0.5 * perimeter * self.slant_height + base_area

# print(RightPyramid.__mro__)
############################################################
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from 
# the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length, **kwargs):
#         super().__init__(length=length, width=length, **kwargs)

# class Cube(Square):
#     def surface_area(self):
#         face_area = super().area()
#         return face_area * 6

#     def volume(self):
#         face_area = super().area()
#         return face_area * self.length

# class Triangle:
#     def __init__(self, base, height, **kwargs):
#         self.base = base
#         self.height = height
#         super().__init__(**kwargs)

#     def tri_area(self):
#         return 0.5 * self.base * self.height

# class RightPyramid(Square, Triangle):
#     def __init__(self, base, slant_height, **kwargs):
#         self.base = base
#         self.slant_height = slant_height
#         kwargs["height"] = slant_height
#         kwargs["length"] = base
#         super().__init__(base=base, **kwargs)

#     def area(self):
#         base_area = super().area()
#         perimeter = super().perimeter()
#         return 0.5 * perimeter * self.slant_height + base_area

#     def area_2(self):
#         base_area = super().area()
#         triangle_area = super().tri_area()
#         return triangle_area * 4 + base_area
###############################################################
# class MyContainer(object):
    
#     def __init__(self):
#         self.storage = {}

#     def __setitem__(self, key, value):
#         self.storage[key] = value
    
#     def __getitem__(self, key):
#         return self.storage[key]
    

# my_container = MyContainer()  
# my_container['a'] = 'b'
# print(my_container['a'])  # b
# # my_container['q']  # KeyError
# ###################################################
# class Foo:
#      pass
# obj = Foo()
# obj.__class__
# type(obj)
# obj.__class__ is type(obj)
#####################################
# class Foo:
#      pass

# x = Foo()

# print(type(x))

# print(type(Foo))
#####################################
# for t in int, float, dict, list, tuple:
#      print(type(t))
##########################################
# Foo = type('Foo', (), {})
# x = Foo()
# print(x)

# >>> class Foo:
#      pass
# ...
# >>> x = Foo()
# >>> x
###########################################
# class Foo:
#      pass
# Bar = type('Bar', (Foo,), dict(attr=100))

# x = Bar()
# print(x.attr)
# print(x.__class__)
# print(x.__class__.__bases__)
##########################################
# >>> Foo = type(
# ...     'Foo',
# ...     (),
# ...     {
# ...         'attr': 100,
# ...         'attr_val': lambda x : x.attr
# ...     }
# ... )

# >>> x = Foo()
# >>> x.attr
# 100
# >>> x.attr_val()
# 100
######################################
# >>> class Foo:
# ...     attr = 100
# ...     def attr_val(self):
# ...         return self.attr
# ...

# >>> x = Foo()
# >>> x.attr
# 100
# >>> x.attr_val()
# 100
########################################
# >>> def f(obj):
# ...     print('attr =', obj.attr)
# ...
# >>> Foo = type(
# ...     'Foo',
# ...     (),
# ...     {
# ...         'attr': 100,
# ...         'attr_val': f
# ...     }
# ... )

# >>> x = Foo()
# >>> x.attr
# 100
# >>> x.attr_val()
# attr = 100


# >>> def f(obj):
# ...     print('attr =', obj.attr)
# ...
# >>> class Foo:
# ...     attr = 100
# ...     attr_val = f
# ...

# >>> x = Foo()
# >>> x.attr
# 100
# >>> x.attr_val()
# attr = 100
###########################################
# >>> class Foo:
# ...     pass
# ...
# >>> f = Foo()

# >>> def new(cls):
# ...     x = object.__new__(cls)
# ...     x.attr = 100
# ...     return x
# ...
# >>> Foo.__new__ = new

# >>> f = Foo()
# >>> f.attr
# 100

# >>> g = Foo()
# >>> g.attr
# 100
#######################################
# Spoiler alert:  This doesn't work!
# >>> def new(cls):
# ...     x = type.__new__(cls)
# ...     x.attr = 100
# ...     return x
# ...
# >>> type.__new__ = new
# Traceback (most recent call last):
#   File "<pyshell#77>", line 1, in <module>
#     type.__new__ = new
# TypeError: can't set attributes of built-in/extension type 'type'
######################################
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         x = super().__new__(cls, name, bases, dct)
#         x.attr = 100
#         return x

# >>> class Foo(metaclass=Meta):
# ...     pass
# ...
# >>> Foo.attr
# 100

# >>> class Bar(metaclass=Meta):
# ...     pass
# ...
# >>> class Qux(metaclass=Meta):
# ...     pass
# ...
# >>> Bar.attr, Qux.attr
# (100, 100)
##########################################
# >>> class Foo:
# ...     def __init__(self):
# ...         self.attr = 100
# ...

# >>> x = Foo()
# >>> x.attr
# 100

# >>> y = Foo()
# >>> y.attr
# 100

# >>> z = Foo()
# >>> z.attr
# 100
##########################################
# >>> class Meta(type):
# ...     def __init__(
# ...         cls, name, bases, dct
# ...     ):
# ...         cls.attr = 100
# ...
# >>> class X(metaclass=Meta):
# ...     pass
# ...
# >>> X.attr
# 100

# >>> class Y(metaclass=Meta):
# ...     pass
# ...
# >>> Y.attr
# 100

# >>> class Z(metaclass=Meta):
# ...     pass
# ...
# >>> Z.attr
# 100
#################################################3
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
# s = Singleton()
# print("Object created", s)
# s1 = Singleton()
# print("Object created", s1)
##################################################
# class MyInt(type):
#     def __call__(cls, *args, **kwds):
#         print("***** Here's My int *****", args)
#         print("Now do whatever you want with these objects...")
#         return type.__call__(cls, *args, **kwds)
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# i = int(4,5)
# print(i.x)
################################
# import sqlite3
# class MetaSingleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#             print(cls._instances)
#         return cls._instances[cls]
# class Database(metaclass=MetaSingleton):
#     connection = None
    
#     def connect(self):
#         if self.connection is None:
#             self.connection = sqlite3.connect("db.sqlite3")
#             self.cursorobj = self.connection.cursor()
#         return self.cursorobj
# db1 = Database().connect()
# db2 = Database().connect()
# print ("Database Objects DB1", db1)
# print ("Database Objects DB2", db2)
    
