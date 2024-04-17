#Program that reads two numbers M and N and print N numbers after M.
m_number=int(input())
n_times_print_number=int(input())
counter=0
while counter<n_times_print_number:
    m_number=m_number+1
    print(m_number)
    counter=counter+1