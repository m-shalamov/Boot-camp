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