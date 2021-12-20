from task import add

result = add.delay(4, 4)
print(result.get(timeout=11))
print("end")
