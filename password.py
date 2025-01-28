def check_password_strength(password):
    return (len(password)>= 8 and
            any(c.isuper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in "!@#$%^&*()" for c in password))
password = input("enter password")
if check_password_strength(password):
    print("strong password")
else:
    print("weak password, create strong one")
def main():
    check_password_strength(password)
main()









