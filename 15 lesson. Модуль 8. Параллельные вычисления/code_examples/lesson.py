###_5(Futures)
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import random

# def task():
#     print('Executing our Task')
#     result = 0
#     i = 0
#     for i in range(10):
#         result = result + i
#     print('I: {}'.format(result))
#     print('Task Executed {}'.format(threading.current_thread()))

# def main():
#     executor = ThreadPoolExecutor(max_workers=3)
#     task1 = executor.submit(task)
#     task2 = executor.submit(task)

# if __name__ == '__main__':
#     main()
#######################################################################
# from concurrent.futures import ThreadPoolExecutor

# def task(n):
#     print('Processing {}'.format(n))

# def main():
#     print('Starting ThreadPoolExecutor')
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         future = executor.submit(task, (2))
#         future = executor.submit(task, (3))
#         future = executor.submit(task, (4))
#     print('All tasks complete')

# if __name__ == '__main__':
#     main()
#######################################################
# import time
# import requests
# from concurrent.futures import ThreadPoolExecutor, as_completed

# URLS = [
# 'https://mail.ru/',
# 'https://realpython.com/python-concurrency/',
# 'https://www.bbc.com/sport/football',
# 'https://www.marvel.com/',
# ]

# def checkStatus(url):
#     print('Attempting to crawl URL: {}'.format(url))
#     response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     return (response.status_code, url)

# def printStatus(statusCode):
#     print('URL Crawled with status code: {}'.format(statusCode))

# def main():
#     with ThreadPoolExecutor(max_workers=3) as executor:

#         tasks = []
#         for url in URLS:
#             task = executor.submit(checkStatus, url)
#             tasks.append(task)

#         for result in as_completed(tasks):
#             printStatus(result.result())

# if __name__ == '__main__':
#     main()
###########################################################

# from concurrent.futures import ThreadPoolExecutor

# values = [2,3,4,5,6,7,8]

# def multiplyByTwo(n):
#     return 2 * n

# def main():
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         results = executor.map(multiplyByTwo, values)

#     for result in results:
#         print(result)

# if __name__ == '__main__':
#     main()

############################################################
# from concurrent.futures import ThreadPoolExecutor

# def task(n):
#     print('Processing {}'.format(n))

# def taskDone(fn):
#     if fn.cancelled():
#         print('Our {} Future has been cancelled'.format(fn.arg))
#     elif fn.done():
#         print('Our Task has completed')

# def main():
#     print('Starting ThreadPoolExecutor')
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         future = executor.submit(task, (2))
#         future.add_done_callback(taskDone)

#     print('All tasks complete')

# if __name__ == '__main__':
#     main()
##################################################################
# INTEGRATING

# import math
# import timeit
# import time
# from threading import Thread
# from functools import partial
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


# a = 0
# b = math.pi/2
# n_jobs = 8
# # f = lambda x:  2
# def f(x): return math.cos(x)
# # f = math.cos
# n_iter = 10000000


# def integrate(f, a, b, *, n_iter=n_iter):
#     acc = 0
#     step = (b - a) / n_iter
#     for i in range(n_iter):
#         acc += f(a + i * step) * step
#     return acc


# def integrate_thread(f, a, b, *, n_jobs, n_iter=n_iter):
#     executor = ThreadPoolExecutor(max_workers=n_jobs)
#     submit = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
#     step = (b - a) / n_jobs
#     fs = [submit(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
#     return sum(item.result() for item in as_completed(fs))


# def integrate_process(f, a, b, *, n_jobs, n_iter=n_iter):
#     executor = ProcessPoolExecutor(max_workers=n_jobs)
#     submit = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
#     step = (b - a) / n_jobs
#     fs = [submit(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
#     return sum(item.result() for item in as_completed(fs))


# def main():

#     integrate_partial_1 = partial(integrate, f=f, a=a, b=b)
#     # print(timeit.repeat(integrate_partial_1, number=100))
#     t = time.time()
#     print(integrate_partial_1())
#     print(time.time() - t)
    
    
#     integrate_partial_2 = partial(integrate_thread, f=f, a=a, b=b, n_jobs=n_jobs)
#     t = time.time()
#     print(integrate_partial_2())
#     print(time.time() - t)
#     # print(timeit.repeat(integrate_partial_2, number=100))

#     integrate_partial_3 = partial(integrate_process, f=f, a=a, b=b, n_jobs=n_jobs)
#     t = time.time()
#     print(integrate_partial_3())
#     print(time.time() - t)
#     # print(timeit.repeat(integrate_partial_3, number=100))

# if __name__ == "__main__":
#     main()
####################################################

# PRACTICE
# import timeit
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
# import math

# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419,
# ]


# def is_prime(n):
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# def main():

#     t1 = timeit.default_timer()
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print("%d is prime: %s" % (number, prime))

#     print(
#         "{} Seconds Needed for ProcessPoolExecutor".format(timeit.default_timer() - t1)
#     )
    
    
    
#     t2 = timeit.default_timer()
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print("%d is prime: %s" % (number, prime))
#     print(
#         "{} Seconds Needed for ThreadPoolExecutor".format(timeit.default_timer() - t2)
#     )
    
    
#     t3 = timeit.default_timer()
#     for number in PRIMES:
#         isPrime = is_prime(number)
#         print("{} is prime: {}".format(number, isPrime))
#     print(
#         "{} Seconds needed for single threaded execution".format(
#             timeit.default_timer() - t3
#         )
#     )


# if __name__ == "__main__":
#     main()


###_10(Integrating)
# import math
# import timeit
# from threading import Thread
# from functools import partial


# def integrate(f, a, b, *, n_iter=10000):
#     acc = 0
#     step = (b - a) / n_iter
#     for i in range(n_iter):
#         acc += f(a + i * step) * step
#     return acc

# def integrate_conc(f, a, b, data, num_of_thread, *, n_iter, n_threads):
#     acc = 0
#     step = (b - a) / n_iter
#     k = num_of_thread
#     for i in range(n_iter//n_threads):
#         acc += f(a + k * step) * step
#         k+=n_threads
#     data[num_of_thread] = acc


# def integrate_threads(f, a, b, *, n_threads=10, n_iter=1000):
#     data = {}
#     threads = [
#         Thread(
#             target=partial(
#                 integrate_conc, f=f, a=a, b=b, data = data, num_of_thread = i, n_iter=n_iter,  n_threads = n_threads
#             )
#         )
#         for i in range(n_threads)
#     ]


#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()
#     return sum(data.values())

# integrate = partial(integrate, f=math.cos, a=0, b=math.pi / 2)
# integrate_threads = partial(integrate_threads, f=math.cos, a=0, b=math.pi / 2)

# # print(integrate_threads(f=math.cos, a=-math.pi / 2, b=math.pi / 2))
# # print(integrate(f=math.cos, a=-math.pi / 2, b=math.pi / 2))
# print(timeit.repeat(integrate, number=1000))
# print(timeit.repeat(integrate_threads, number=1000))
#ASYNCIO EX###########################################################
# import asyncio
# import time 
# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

#SYNC EX###################################
# import time

# def count():
#     print("One")
#     time.sleep(1)
#     print("Two")

# def main():
#     for _ in range(3):
#         count()

# if __name__ == "__main__":
#     s = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")










#Ex##################################################################
# import asyncio
# import random

# # ANSI colors
# c = (
#     "\033[0m",   # End of color
#     "\033[36m",  # Cyan
#     "\033[91m",  # Red
#     "\033[35m",  # Magenta
# )

# async def makerandom(idx: int, threshold: int = 6) -> int:
#     print(c[idx + 1] + f"Initiated makerandom({idx}).")
#     i = random.randint(0, 10)
#     while i <= threshold:
#         print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
#         await asyncio.sleep(idx + 1)
#         i = random.randint(0, 10)
#     print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
#     return i

# async def main():
#     res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
#     return res

# if __name__ == "__main__":
#     r1, r2, r3 = asyncio.run(main())
#     print()
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}")





#chaining ######################################
# import asyncio
# import random
# import time

# async def part1(n: int) -> str:
#     i = random.randint(0, 10)
#     print(f"part1({n}) sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-1"
#     print(f"Returning part1({n}) == {result}.")
#     return result

# async def part2(n: int, arg: str) -> str:
#     i = random.randint(0, 10)
#     print(f"part2{n, arg} sleeping for {i} seconds.")
#     await asyncio.sleep(i)
#     result = f"result{n}-2 derived from {arg}"
#     print(f"Returning part2{n, arg} == {result}.")
#     return result

# async def chain(n: int) -> None:
#     start = time.perf_counter()
#     p1 = await part1(n)
#     p2 = await part2(n, p1)
#     end = time.perf_counter() - start
#     print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

# async def main(*args):
#     await asyncio.gather(*(chain(n) for n in args))

# if __name__ == "__main__":
#     import sys
#     random.seed(444)
#     args = [1, 2, 3]
#     start = time.perf_counter()
#     asyncio.run(main(*args))
#     end = time.perf_counter() - start
#     print(f"Program finished in {end:0.2f} seconds.")

