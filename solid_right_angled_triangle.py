#Given an integer number (N) as input.
# Write a program to print the right-angled triangular pattern of N lines using an asterisk(*) character.
n=int(input())

counter=1
while counter<=n:
       print("* " *counter)
       counter=counter+1