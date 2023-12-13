from functools import lru_cache


@lru_cache
def calculate_sum():
    num = int(input("Введите число: "))
    if num > 0:
        return num + calculate_sum()
    else:
        return 0


sum_positive_numbers = calculate_sum()
print(f'Сумма положительных чисел равна:', sum_positive_numbers)
