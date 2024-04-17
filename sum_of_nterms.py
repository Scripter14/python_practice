# Program to sum of n terms in series
#x
x = int(input())
n = int(input())

sum_of_terms = 0
power = 1

for i in range(0, n):
    raise_to_power = x ** power
    power = power + 2

    x = (-x)
    sum_of_terms = sum_of_terms + raise_to_power

print(sum_of_terms)
