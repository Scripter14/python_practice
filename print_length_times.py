#Write a program that reads a string and prints the first character of the given string on N lines where Nis the length of given string
given_string=input()
N_length_of_given_string=len(given_string)
counter=0
while counter<N_length_of_given_string:
 print(given_string[0])
 counter=counter+1