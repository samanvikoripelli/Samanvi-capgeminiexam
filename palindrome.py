def is_palindrome(value):
    if type(value)==int:
        value = str(value)
        value = value.replace("","").lower()
        return value == value[::-1]
    while True:
        value = input("enter string or number(or 'q' to quit):")
        if value.lower() == 'q':
            break
        if is_palindrome(value):
            print(f"{value} is a palindrome")
        else:
            print(f"{value} is not a palindrome")
value = input("enter a string or number")
is_palindrome(value)