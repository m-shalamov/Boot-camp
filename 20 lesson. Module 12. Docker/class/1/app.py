import time

file_name = "./volumes/file.txt"
with open(file_name, "a") as f:
    for i in range(10):
        f.write(str(i) + "\n")
time.sleep(1000)
