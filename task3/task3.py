# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def unique_num(list):
    new_list = []
    for i in range(0, len(list)):
        if not list[i] in new_list:
            new_list.append(list[i])
    return new_list


num_list = [1, 2, 3, 3, 4, 5, 5, 8, 3, 1, 2]
new_list = unique_num(num_list)
print(new_list)

#=================== пример выполнения с семинара через словарь и counter

# from collections import Counter

# nums = input('Введите числа через пробел: ').split()
# counts = Counter(nums)
# print([i for i in counts if counts[i] == 1])


# res = []
# for key in counts:
#     if counts[key] == 1:
#         res.append(key)
# print(res)
