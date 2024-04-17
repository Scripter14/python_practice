# Write a program that reads the number N  and finds the count of digits from 1 to N.
# numbers from 1 to 9 are single digits  And numbers from 10 to 99 are double digits and so on.
n = int(input())
digit_count = 0
for i in range(1, n + 1):
    length_of_number = len(str(i))
    digit_count = digit_count + length_of_number
print(digit_count)


