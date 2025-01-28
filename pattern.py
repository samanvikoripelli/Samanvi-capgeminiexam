n = int(input("enter the numberof rows"))
for i in range(1,n+1):
    print('*' * i)
reverse = input("print the pattern in reverse?(yes/no)").lower()
if reverse == 'yes':
    for i in range(n - 1, 0, -1):
        print('*' * i)