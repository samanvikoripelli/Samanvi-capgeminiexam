def fizzbuzz():
    for num in range(1,101):
        if num % 3 is 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("fizz")
        else:
            print(num)
def main():
    fizzbuzz()
main()