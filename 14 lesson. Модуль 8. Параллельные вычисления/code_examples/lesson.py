###_1(Queue)


# import queue
# import random
# import time
# from collections import defaultdict, Counter
# from threading import Thread, Lock
# from queue import Queue, Empty


# class Game(Thread):
#     def __init__(self, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.players = []
#         self.bullets = bullets
#         self.total = defaultdict(int)
#         self.queue = Queue(maxsize=3)

#     def add_player(self, name):
#         self.players.append(Player(name=name, bullets=self.bullets, queue=self.queue))

#     def run(self):
#         for player in self.players:
#             player.start()
#         while True:
#             try:
#                 result = self.queue.get(timeout=1)
#                 # print("got one result\n", flush=True)
#                 self.total[result] += 1
#             except Empty:
#                 # print("no results for 1 sec\n", flush=True)
#                 if not any(player.is_alive() for player in self.players):
#                     break

#         for player in self.players:
#             player.join()


# class Player(Thread):

#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, queue, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets
#         self.queue = queue

#     def run(self):
#         for bullet in range(1, self.bullets + 1):

#             shot = random.choice(Player.targets)
#             self.result[shot] += 1
#             # if self.queue.full():
#             #     pass
#                 # print("full\n", flush=True)
#             self.queue.put(shot)
#             # print("gave\n", flush=True)


# def get_total_dict(players):
#     total = {}
#     for player in players:
#         total = dict(Counter(total) + Counter(player.result))
#     return total


# def get_total_number(players):
#     total = 0
#     for player in players:
#         total = total + sum(player.result.values())
#     return total


# player_names = [
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
# ]


# game = Game(100000)
# for name in player_names:
#     game.add_player(name=name)

# game.start()
# game.join()
# print(game.total)
# print(get_total_dict(game.players))


###_2(Daemons)

# import threading
# import time
# def standardThread():
#     print('Starting my Standard Thread')
#     time.sleep(20)
#     print('Ending my standard thread')
# def daemonThread():
#     while True:
#       print('Sending Out Heartbeat Signal')
#       time.sleep(2)
# if __name__ == '__main__':
#   standardThread = threading.Thread(target=standardThread)
#   daemonThread = threading.Thread(target=daemonThread)
#   daemonThread.setDaemon(True)
#   daemonThread.start()

#   standardThread.start()


###_4(Deadlock)

# import threading
# import time
# import random


# class Philosopher(threading.Thread):
#     def __init__(self, name, leftFork, rightFork):
#         print("Our Philosopher Has Sat Down At the Table")
#         threading.Thread.__init__(self)
#         self.leftFork = leftFork
#         self.rightFork = rightFork
#         self.name = name
#     def run(self):
#         print(f"Philosopher: {threading.current_thread()} has started thinking")
#         while True:
#             # time.sleep(random.randint(1,5))
#             print(f"Philosopher {threading.current_thread()} has finished thinking\n")
#             self.leftFork.acquire()
#             # time.sleep(random.randint(1, 5))
#             print(f"Philosopher {threading.current_thread()} has acquired the left fork\n")
#             self.rightFork.acquire()
#             print(f"Philosopher {threading.current_thread()} has attained both forks, currently eating\n")
#             self.rightFork.release()
#             print(f"Philosopher {threading.current_thread()} has released the right fork\n")
#             self.leftFork.release()
#             print(f"Philosopher {threading.current_thread()} has released the left fork\n")
#     def __str__(self) -> str:
#         return self.name

# threads = []
# names = ["Tom", "Jack", "Rassel"]
# n = len(names)
# locks = [threading.Lock() for _ in range(n)]
# for i in range(n):
#     thread = Philosopher(names[i], locks[i], locks[(i+1)%n])
#     thread.start()
# for _ in range(n):
#     thread.join()


###_4(Multiprocessing)
# import queue
# import random
# import time
# from collections import defaultdict, Counter
# from multiprocessing import Process, Pipe, Queue
# from queue import Queue, Empty

# total = defaultdict(int)  # 0


# class Player(Process):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         global total
#         for bullet in range(1, self.bullets + 1):

#             shot = random.choice(Player.targets)

#             self.result[shot] += 1
#             total[shot] += 1


# if __name__ == "__main__":
#     def processes_work(players):
#         for player in players:
#             player.start()
#         for player in players:
#             player.join()


#     def get_total_dict(players):
#         total = {}
#         for player in players:
#             total = dict(Counter(total) + Counter(player.result))
#         return total


#     # def get_total_number(players):
#     #     total = 0
#     #     for player in players:
#     #         total = total + sum(player.result.values())
#     #     return total


#     player_names = [
#         "Tom",
#         "Jack",
#         "Anna",
#         "Helen",
#     ]

#     players = [Player(name, 10000) for name in player_names]
#     processes_work(players)

#     print(total)
#     print(get_total_dict(players))


#############################################################
# import queue
# import random
# import time
# from collections import defaultdict, Counter
# from multiprocessing import Process, Pipe, Queue
# from queue import Empty

# # total = defaultdict(int)  # 0


# class Player(Process):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, connection,  *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets
#         self.connection = connection
#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             shot = random.choice(Player.targets)
#             self.result[shot] += 1
#         ans = 0
#         for key, val in self.result.items():
#             ans+=key*val
#         self.connection.send(ans)
#         self.connection.close()

# if __name__ == "__main__":
#     def processes_work(players):
#         for player in players:
#             player.start()
#         for player in players:
#             player.join()


#     def get_total_dict(players):
#         total = {}
#         for player in players:
#             total = dict(Counter(total) + Counter(player.result))
#         return total


#     def get_total_number(players):
#         total = 0
#         for player in players:
#             total = total + sum(player.result.values())
#         return total


#     player_names = [
#         "Tom",
#         "Jack",
#         "Anna",
#         "Helen",
#     ]

#     # players = [Player(name, 10000) for name in player_names]

#     players = []
#     pipes = []
#     for name in player_names:
#         parent, child = Pipe()
#         players.append(Player(name, 100000000, connection = child))
#         pipes.append(parent)
#     processes_work(players)


#     total = 0
#     for connection in pipes:
#         total += connection.recv()

#     print(total)
# print(get_total_dict(players))


###################################################
# import random
# import time
# from collections import defaultdict, Counter
# from multiprocessing import Process, Queue
# from queue import Empty


# class Game(Process):
#     def __init__(self, bullets, player_names, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.players = []
#         self.bullets = bullets
#         self.player_names = player_names
#         self.total = defaultdict(int)
#         self.queue = Queue(maxsize=3)

#     def __add_player(self, name):
#         self.players.append(Player(name=name, bullets=self.bullets, queue=self.queue))

#     def run(self):
#         for name in self.player_names:
#             self.__add_player(name)
#         for player in self.players:
#             player.start()
#         while True:
#             try:
#                 result = self.queue.get(timeout=0.1)
#                 self.total[result] += 1
#             except Empty:
#                 # print("no results for 1 sec\n", flush=True)
#                 if not any(player.is_alive() for player in self.players):
#                     break

#         for player in self.players:
#             player.join()
#         print(self.total)

# class Player(Process):

#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, queue, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets
#         self.queue = queue

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             shot = random.choice(Player.targets)
#             self.result[shot] += 1
#             self.queue.put(shot)


# if __name__=="__main__":
#     player_names = [
#         "Tom",
#         "Jack",
#         "Anna",
#         "Helen",
#     ]
#     game = Game(1000, player_names)
#     # for name in player_names:
#     #     game.add_player(name=name)

#     game.start()
#     game.join()


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


