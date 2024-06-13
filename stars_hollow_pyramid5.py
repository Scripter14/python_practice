n = int(input())

for i in range(1, n + 1):
    if i == 1:
        left_spaces = " " * 2 * (n - 1)
        row = left_spaces + "*"
    elif i == n:
        row = "* " * n
    else:
        left_spaces = (" ") * 2 * (n - i)
        middle_spaces = " " * (2 * (i - 1) - 1)
        row = left_spaces + "*" + middle_spaces + "*"

    print(row)

'''output

4
      *
    * *
  *   *
* * * * 




'''