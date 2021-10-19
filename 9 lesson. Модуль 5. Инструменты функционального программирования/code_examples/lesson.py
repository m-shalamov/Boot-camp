# def chain(*iterables):
#     for i in iterables:
#         yield from i


# s = "ABC"
# t = tuple(range(3))
# list(chain(s, t))
def f(x):
    value = 0
    while True:
        new_value = yield x + new_value
        value = new_value or value


adder = f(2)
print(next(adder))

print(adder.send(23))
