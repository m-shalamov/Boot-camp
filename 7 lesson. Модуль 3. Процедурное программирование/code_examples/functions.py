import warnings


def f(n):
    if n == 3:
        warnings.warn("warning", category=RuntimeWarning)
    print(n)


warnings.simplefilter("error")

for i in range(5):
    try:
        f(i)
    except:
        print("done")
