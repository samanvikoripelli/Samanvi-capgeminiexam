def multiplication_table(number):
    print(f"multiplication table for {number}:")
    for i in range(1,11):
        print(f"{number}*{i} = {number*i}")
def main(): 
    number = int(input("enter the number"))
    multiplication_table(number)
main()