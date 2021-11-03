###_1(Queue)

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
######################################################################
# from queue import Queue

# def do_stuff(q):
#     while not q.empty():
#         print (q.get())
#         q.task_done()

# q = Queue(maxsize=0)

# for x in range(20):
#     q.put(x)

# do_stuff(q)
####################################
# from queue import Queue
# import queue
# from threading import Thread

# def do_stuff(q):
#     while True:
#         try:
#             print(q.get(timeout = 0.1))
#             q.task_done()
#         except queue.Empty:
#             break
# q = Queue(maxsize=0)
# num_threads = 10

# for i in range(num_threads):
#     worker = Thread(target=do_stuff, args=(q,))
#     # worker.setDaemon(True)
#     worker.start()

# for x in range(100):
#     q.put(x)

# q.join()
# print("end")
#################################################################









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
