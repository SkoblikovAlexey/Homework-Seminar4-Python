# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def is_simple_number(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    else:
        for i in range(2, num):
            if not num % i == 0:
                continue
            else:
                return False
        return True


def find_simple_factors(number):
    new_list = []
    for i in range(1, number + 1):
        if number % i == 0 and is_simple_number(i):
            new_list.append(i)
    return new_list


a = int(input("Введите число N: "))
simple_num_list = find_simple_factors(a)
print(f'Список простых множителей введенного числа {a}: {simple_num_list}')
