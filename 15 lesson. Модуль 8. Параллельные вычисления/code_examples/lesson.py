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











#queue##############################

# import asyncio
# import random
# import time

# async def makeitem(size: int = 5) -> str:
#     return str(random.randint(0, size))

# async def randsleep(caller=None) -> None:
#     i = random.randint(0, 10)
#     if caller:
#         print(f"{caller} sleeping for {i} seconds.")
#     await asyncio.sleep(i)

# async def produce(name: int, q: asyncio.Queue) -> None:
#     n = random.randint(0, 10)
#     for _ in range(n):  # Synchronous loop for each single producer
#         await randsleep(caller=f"Producer {name}")
#         i = await makeitem()
#         t = time.perf_counter()
#         await q.put((i, t))
#         print(f"Producer {name} added <{i}> to queue.")

# async def consume(name: int, q: asyncio.Queue) -> None:
#     while True:
#         await randsleep(caller=f"Consumer {name}")
#         i, t = await q.get()
#         now = time.perf_counter()
#         print(f"Consumer {name} got element <{i}>"
#               f" in {now-t:0.5f} seconds.")
#         q.task_done()

# async def main(nprod: int, ncon: int):
#     q = asyncio.Queue()
#     #create_task does just the submitting, it should have probably been called start_coroutine or something like that.
#     producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
#     consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
#     # asyncio.gather is not the only way to achieve concurrency in asyncio.
#     # It's just a utility function that makes it easier to wait for a number of coroutines to all complete, and submit them to the event loop at the same time.
#     await asyncio.gather(*producers)
#     await q.join()  # Implicitly awaits consumers, too
#     for c in consumers:
#         c.cancel()

# if __name__ == "__main__":
#     random.seed(444)
#     start = time.perf_counter()
#     asyncio.run(main(nprod=5, ncon=10))
#     elapsed = time.perf_counter() - start
#     print(f"Program completed in {elapsed:0.5f} seconds.")







###########################################
# from queue import  Queue
# q = Queue()
# q.put(3)
# q.get()
# q.put(44)
# q.task_done()








#PARSING SYNC###########################################
import json
import time
import requests
from bs4 import BeautifulSoup
import datetime
import csv


start_time = time.time()


def get_data():
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"data/labirint_{cur_time}.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название книги",
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Цена без скидки",
                "Процент скидки",
                "Наличие на складе"
            )
        )

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)

    books_data = []
    for page in range(1, pages_count + 1):
    # for page in range(1, 2):
        url = f"{url}&page={page}"

        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        books_items = soup.find("tbody", class_="products-table__body").find_all("tr")

        for bi in books_items:
            book_data = bi.find_all("td")

            try:
                book_title = book_data[0].find("a").text.strip()
            except:
                book_title = "Нет названия книги"

            try:
                book_author = book_data[1].text.strip()
            except:
                book_author = "Нет автора"

            try:
                # book_publishing = book_data[2].text
                book_publishing = book_data[2].find_all("a")
                book_publishing = ":".join([bp.text for bp in book_publishing])
            except:
                book_publishing = "Нет издательства"

            try:
                book_new_price = int(book_data[3].find("div", class_="price").find("span").find("span").text.strip().replace(" ", ""))
            except:
                book_new_price = "Нет нового прайса"

            try:
                book_old_price = int(book_data[3].find("span", class_="price-gray").text.strip().replace(" ", ""))
            except:
                book_old_price = "Нет старого прайса"

            try:
                book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)
            except:
                book_sale = "Нет скидки"

            try:
                book_status = book_data[-1].text.strip()
            except:
                book_status = "Нет статуса"

            # print(book_title)
            # print(book_author)
            # print(book_publishing)
            # print(book_new_price)
            # print(book_old_price)
            # print(book_sale)
            # print(book_status)
            # print("#" * 10)

            books_data.append(
                {
                    "book_title": book_title,
                    "book_author": book_author,
                    "book_publishing": book_publishing,
                    "book_new_price": book_new_price,
                    "book_old_price": book_old_price,
                    "book_sale": book_sale,
                    "book_status": book_status
                }
            )

            with open(f"data/labirint_{cur_time}.csv", "a", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        book_title,
                        book_author,
                        book_publishing,
                        book_new_price,
                        book_old_price,
                        book_sale,
                        book_status
                    )
                )

        print(f"Обработана {page}/{pages_count}")
        time.sleep(1)

    with open(f"data/labirint_{cur_time}.json", "w") as file:
        json.dump(books_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")


if __name__ == '__main__':
    main()