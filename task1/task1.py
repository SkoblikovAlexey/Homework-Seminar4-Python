# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def calc_factor(num):
    result = 0
    while num % 1 > 0:
        num *= 10
        result += 1
    return result


fract_accur = float(input("Введите необходимую точность: "))
rounded_pi = round(math.pi, calc_factor(fract_accur))
print(rounded_pi)

