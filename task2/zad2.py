def custom_sort(A, B):
    count = {}
    for num in A:
        count[num] = count.get(num, 0) + 1

    result = []
    for num in B:
        result.extend([num]*count[num])

    remaining = sorted([num for num in A if num not in B], reverse=True)
    result.extend(remaining)

    return result

A = list(map(int, input("Введите массив A через пробел: ").split()))
B = list(map(int, input("Введите массив B через пробел (уникальные элементы): ").split()))

sorted_A = custom_sort(A, B)
print("Отсортированный массив A:", sorted_A)
