# Threads

###_1(Functions)
# import random
# import time
# from collections import defaultdict
# from threading import Thread


# def game(name, bullets, result):
#     for bullet in range(1, bullets + 1):
#         print(f"{name} is shooting with the bullet #{bullet}. Waiting for the fire", flush=True)
#         _ = 10000 ** random.randint(100, 10000)
#         shot = random.choice(targets)
#         if shot == 0:
#             print(f"{name} got nothing", flush=True)
#             result[shot] += 1
#         else:
#             print(f"{name} got {shot}", flush=True)
#             result[shot] += 1


# targets = (0, 10, 20, 50, 100)
# result_Tom = defaultdict(int)
# result_Jack = defaultdict(int)
# Tom = {"name": "Tom", "bullets": 100, "result": result_Tom}
# Jack = {"name": "Jack", "bullets": 100, "result": result_Jack}
# thread = Thread(target=game, kwargs=Tom)
# thread.start()
# game(**Jack)
# thread.join()
# for name, _, result in [Tom.values(), Jack.values()]:
#     print(f"{name} got: ", flush=True)
#     for shot, count in result.items():
#         print(f"{shot} : {count}", flush=True)


###_2(Classes)
# import random
# import time
# from collections import defaultdict
# from threading import Thread


# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             print(
#                 f"{self.name} is shooting with the bullet #{bullet}. Waiting for the fire\n",
#                 flush=True,
#             )
#             _ = 10000 ** random.randint(100, 10000)
#             shot = random.choice(Player.targets)
#             if shot == 0:
#                 print(f"{self.name} got nothing\n", flush=True)
#                 self.result[shot] += 1
#             else:
#                 print(f"{self.name} got {shot}\n", flush=True)
#                 self.result[shot] += 1


# Tom = Player(**{"name": "Tom", "bullets": 10})
# Jack = Player(**{"name": "Jack", "bullets": 10})
# print("The game has begun\n")
# Tom.start()
# Jack.start()
# print("Waiting till the end\n")
# Tom.join()
# Jack.join()
# print("The game has finished\n")

# for player in [Tom, Jack]:
#     print(f"{player.name} got: ", flush=True)
#     for shot, count in player.result.items():
#         print(f"{shot} : {count}", flush=True)


###_3(Exceptions)
# import random
# import time
# from collections import defaultdict
# from threading import Thread


# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         try:
#             self.__game()
#         except Exception as e:
#             print(f"The exception is detected: {e.args}")

#     def __game(self):
#         for bullet in range(1, self.bullets + 1):
#             print(
#                 f"{self.name} is shooting with the bullet #{bullet}. Waiting for the fire\n",
#                 flush=True,
#             )
#             _ = 10000 ** random.randint(100, 10000)
#             shot = random.choice(Player.targets)
#             print(f"the system equals {1/random.randint(0,4)}\n", flush=True)
#             if shot == 0:
#                 print(f"{self.name} got nothing\n", flush=True)
#                 self.result[shot] += 1
#             else:
#                 print(f"{self.name} got {shot}\n", flush=True)
#                 self.result[shot] += 1


# Tom = Player(**{"name": "Tom", "bullets": 10})
# Jack = Player(**{"name": "Jack", "bullets": 10})
# print("The game has begun\n")
# Tom.start()
# Jack.start()
# print("Waiting till the end\n")
# Tom.join()
# Jack.join()
# print("The game has finished\n")

# for player in [Tom, Jack]:
#     print(f"{player.name} got: ", flush=True)
#     for shot, count in player.result.items():
#         print(f"{shot} : {count}", flush=True)


















###_4(GIL. Time checking)
# import random
# import time
# from collections import defaultdict
# from threading import Thread


# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             # print(
#             #     f"{self.name} is shooting with the bullet #{bullet}. Waiting fot the result\n",
#             #     flush=True
#             # )
#             _ = 10000 * random.randint(100, 100000)
#             shot = random.choice(Player.targets)
#             # print(f"{self.name} got {shot}\n", flush=True)
#             self.result[shot] += 1

# def time_check(f):
#     def inner(*args, **kwargs):
#         start = time.time()
#         f(*args, **kwargs)
#         end = time.time()
#         delta_time = end - start
#         print(f"The time is {delta_time}")
#     return inner

# @time_check
# def threads_work(players):
#     for player in players:
#         player.start()
#     for player in players:
#         player.join()

# @time_check
# def work(players):
#     for player in players:
#         player.run()


# players_names = ["Tom", "Jack", "Ann", "Helen"]

# players = [Player(name, 1000) for name in players_names]

# # work(players)
# threads_work(players)








###_5(lock)
# Importing the threading module
# import threading

# deposit = 100
# k = 100000
# lock = threading.Lock()


# def add():
#     global deposit
#     for i in range(k):
#         lock.acquire()
#         deposit += 10
#         lock.release()


# def pay():
#     global deposit
#     for i in range(k):
#         lock.acquire()
#         deposit -= 10
#         lock.release()

# t1 = threading.Thread(target=add)
# t2 = threading.Thread(target=pay)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(deposit)

###_6(Queue downloading example)
# import queue
# import threading
# import random
# import requests
# import time


# def save_image(id, url):
#     with open(f"data\\pic{id}.jpg", "wb") as image:
#         response = requests.get(url)
#         image.write(response.content)
#         # for block in response.iter_content(1024):
#         #     if not block:
#         #         break
#         #     image.write(block)


# def consumer(q):
#     while True:
#         try:
#             id = q.get(timeout = 0.1)
#             result = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
#             url = result.json()["thumbnailUrl"]
#             save_image(id, url)
#             print(f"Save image {id}")
#         except queue.Empty:
#             if not any(producer.is_alive() for producer in producers):
#                 break


# def producer(q, arr):
#     for i in range(len(arr)):
#         id = random.choice(arr)
#         arr.remove(id)
#         q.put(id)

# NUM_CUNSOMERS = 16
# NUM_PRODUCERS = 2
# q = queue.Queue()
# workers = []
# producers = []
# arr_1 = [item for item in range(1, 101)]
# arr_2 = [item for item in range(101, 201)]
# arr = [arr_1, arr_2]



# for i in range(NUM_CUNSOMERS):
#     worker = threading.Thread(target=consumer, args=(q,))
#     worker.start()
#     workers.append(worker)

# for i in range(NUM_PRODUCERS):
#     worker = threading.Thread(target=producer, args=(q,arr[i]))
#     worker.start()
#     producers.append(worker)


# for w in workers:
#     w.join()

# for w in producers:
#     w.join()



