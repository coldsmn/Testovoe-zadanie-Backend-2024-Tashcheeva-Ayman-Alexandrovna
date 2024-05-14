def sort_array(arr):
    arr.sort()
    return arr

arr = list(map(int, input("Введите целые числа через пробел: ").split()))
print("Отсортированный массив:", sort_array(arr))
