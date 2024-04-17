given_number = int(input())
first_input = int(input())
greatest_number = first_input
for i in range(1, given_number):
    n_inputs = int(input())
    if n_inputs > greatest_number:
        greatest_number = n_inputs
print(greatest_number)
