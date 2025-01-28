def string_analyze(n):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    vowel_count = consonant_count = digit_count = special_count = 0
    for char in n:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():
            special_count += 1
    return vowel_count,consonant_count,digit_count,special_count,n[::-1]
user_input = input("enter a string")
vowels,consonants,digits,specials,reversed_str = string_analyze(user_input)
print(f"Vowels {vowels},Consonants {consonants},Digits {digits},Special characters{specials}")
print(f"Reversed String {reversed_str}")