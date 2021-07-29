# class House:

# 	def __init__(self, price):
# 		self._price = price


# class House:
#     def __init__(self, price):
#         self._price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, new_price):
#         if new_price > 0 and (
#             isinstance(new_price, float) or isinstance(new_price, int)
#         ):
#             self._price = new_price
#         else:
#             print("Please enter a valid price")

#     @price.deleter
#     def price(self):
#         del self._price


# obj = House(2000)
# # Access value
# obj.price

# # Modify value
# obj.price = 40000

# del obj.price

# # Changed from obj.price
# obj.get_price()

# # Changed from obj.price = 40000
# obj.set_price(40000)
## PRACTICE
# Для класса Employee написать @fullname.setter и @fullname.deleter,
# который будет утсанавливать NULL значения для self.first и self.last
# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
    
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None


# emp_1 = Employee('John', 'Smith')
# emp_1.fullname = "Corey Schafer"

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# del emp_1.fullname
