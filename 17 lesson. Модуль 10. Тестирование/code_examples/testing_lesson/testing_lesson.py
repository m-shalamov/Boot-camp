##########################TESTING
def my_sort(arr):
    """
    Функция сортировки списков

    >>> my_sort([3,2,1])
    [1, 2, 3]
    >>> my_sort([3,2,22])
    [2, 3, 22]
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

## MANUAL TESTS

# print(my_sort([3, 4, 2, 8, 1, 6, 4]))
# print(my_sort([3, 4, 5]))
# print(my_sort([3, 2, 1]))
# print(my_sort([]))
# print(my_sort([9, 3, -7, 2]))

# if my_sort([3, 4, 2, 8, 1, 6, 4]) != [1, 2, 3, 4, 4, 6, 8]:
#     print('Ошибка!')
# if my_sort([3, 4, 5]) != [3, 4, 5]:
#     print('Ошибка!')
# if my_sort([3, 2, 1]) != [1, 2, 3]:
#     print('Ошибка!')
# if my_sort([]) != []:
#     print('Ошибка!')
# if my_sort([9, 3, -7, 2]) != [-7, 2, 3, 9]:
#     print('Ошибка!')

# оператор assert - англ. "утверждение"
# assert my_sort([3, 4, 2, 8, 1, 6, 4]) == [1, 2, 3, 4, 4, 6, 8]

# # можно еще писать сообщение, детализирующее возможную ошибку
# assert my_sort([3, 4, 2, 8, 1, 6, 4]) == [1, 2, 3, 4, 4, 6, 8], 'не работает сортировка целых положительных'

## DOCTEST

import doctest
doctest.testmod()


## UNITTEST
# import unittest


# class MySortTest(unittest.TestCase):
#     # нужно отнаследоваться от этого класса, что бы заработала магия тестирования

#     # проверяющие методы должны начинаться с test_
#     def test_normal(self):
#         # запускаем тестируемую функцию
#         result = my_sort([3, 4, 2, 8, 1, 6, 4])
#         # проверяем что она вернула
#         self.assertEqual(result, [1, 2, 3, 4, 4, 6, 8])

#     # в именах методов-проверок очень желательно указывать
#     # какой вариант они проверяют
#     def test_sorted(self):
#         result = my_sort([3, 4, 5])
#         # так же можно писать детализирующее сообщение
#         self.assertEqual(result, [3, 4, 5], 'не работает сортировка отсортированного списка')

#     # и так далее - записываем все возможные случаи
#     def test_reversed(self):
#         result = my_sort([3, 2, 1])
#         self.assertEqual(result, [1, 2, 3])

#     def test_empty(self):
#         result = my_sort([])
#         self.assertEqual(result, [])

#     def test_with_negative(self):
#         result = my_sort([9, 3, -7, 2])
#         self.assertEqual(result, [-7, 2, 3, 9])


# if __name__ == '__main__':
#     # запускам автодискавер тестов
#     unittest.main()
## PRACTICE

#Write unit tests for your function counting the sum of an array
# import unittest
# from my_arrsum import my_arrsum


# class MySortTest(unittest.TestCase):
#     def test_numbers(self):
#         result = my_arrsum([1, 5, 2, 4])
#         self.assertEqual(result, 12)

#     def test_reversed(self):
#         result = my_arrsum([1, 2, 3])
#         self.assertEqual(result, 6)

#     def test_empty(self):
#         result = my_arrsum([])
#         self.assertEqual(result, 0)

#     def test_negative(self):
#         result = my_arrsum([8, -1, -2, 5])
#         self.assertEqual(result, 10)


# if __name__ == "__main__":
#     unittest.main()
#Write unit tests for your class counting an area and a perimeter of a reactangle
