# class Car:
#     def __init__(self, brand, color, price, max_speed):
#         self.color = color
#         self.price = price
#         self.brand = brand
#         self.max_speed = max_speed
#         self.current_speed = 0
#     def go(self):
#         self.current_speed += 10
#     def stop(self):
#         self.current_speed -= 10
#     def show(self):
#         print(self.brand, self.color, self.price, self.max_speed, self.current_speed)
# my_car = Car("BMW","green", 100000, 300)


# setattr(my_car, 'x', 9)
# my_car.y = 99
# delattr(my_car, "brand")
# my_car1 = Car("BMW","green", 100000, 300)
# my_car.show()
# my_car1 = Car("BMW","green", 100000, 300)

from decimal import *

getcontext().prec = 1000
print(Decimal(7).sqrt())
