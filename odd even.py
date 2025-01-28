def seperate_odd_even(numbers):
    even_numbers = []
    odd_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return even_numbers, odd_numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
even_numbers, odd_numbers = seperate_odd_even(numbers)
print("even numbers:",even_numbers)
print("odd numbers:", odd_numbers)