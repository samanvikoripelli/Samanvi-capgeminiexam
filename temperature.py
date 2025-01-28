def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celcius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return(fahrenheit - 32) * 5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return(kelvin - 273.15) * 9/5 + 32
print("temperature conversion tool")
print("1: celsius to fahrenheit")
print("2:celsius to kelvin")
print("3:fahrenheit to celsius")
print("4:fahrenheit to kelvin")
print("5:kelvin to celsius")
print("6:kelvin to fahrenheit")
choice = int(input("choose a conversion(1-6):"))
temp = float(input("enter the temperature:"))
if choice == 1:
    print(f"result:{celsius_to_fahrenheit(temp)} F")
elif choice == 2:
    print(f"result:{celcius_to_kelvin(temp)} K")
elif choice == 3:
    print(f"result:{fahrenheit_to_celsius(temp)} C")
elif choice == 4:
    print(f"result:{fahrenheit_to_kelvin(temp)} K")
elif choice == 5:
    print(f"result:{kelvin_to_celsius(temp)} C")
elif choice == 6:
    print(f"result:{kelvin_to_fahrenheit(temp)} F")
else:
    print("invalid choice")