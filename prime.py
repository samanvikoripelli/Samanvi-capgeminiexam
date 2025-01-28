def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
        return True
def find_prime(start,end):
    print(f"prime numbers between {start} and {end}:")
    for num in range(start,end+1):
        if is_prime(num):
            print(num)
start = int(input("enter starting number"))
end = int(input("enter ending number"))
find_prime(start,end)