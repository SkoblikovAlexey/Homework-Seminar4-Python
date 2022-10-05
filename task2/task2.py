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
    num = number
    if num == 1:
        return new_list
    else:    
        for i in range(1, num + 1):
            if num % i == 0 and is_simple_number(i):
                new_list.append(i)
                num = int(num / i)   
                break    
        return new_list + find_simple_factors(num)


a = int(input("Введите число N: "))
simple_num_list = find_simple_factors(a)
print(f'Список простых множителей введенного числа {a}: {simple_num_list}')
