def max_sum_of_two_nums(nums):
    if len(nums) < 2:
        return None
    return sum(sorted(nums)[-2:])

# Ввод списка целых чисел
num_list = list(map(int, input("Введите список целых чисел через пробел: ").split()))

result = max_sum_of_two_nums(num_list)
if result is None:
    print("В списке меньше двух чисел, нельзя вычислить сумму двух наибольших чисел.")
else:
    print("Наибольшая сумма двух чисел в списке:", result)
