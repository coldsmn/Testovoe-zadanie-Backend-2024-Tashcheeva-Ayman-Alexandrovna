def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Получаем отсортированный список от пользователя
arr = list(map(int, input("Введите отсортированный список чисел через пробел: ").split()))

# Получаем элемент для поиска от пользователя
target = int(input("Введите элемент для поиска: "))

# Выполняем бинарный поиск
result_index = binary_search(arr, target)

if result_index != -1:
    print(f"Элемент {target} найден в списке по индексу {result_index}.")
else:
    print(f"Элемент {target} не найден в списке. По индеку -1")