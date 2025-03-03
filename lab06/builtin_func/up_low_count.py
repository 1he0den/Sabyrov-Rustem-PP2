def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    return upper_count, lower_count

user_input = input("Enter a string: ")

upper, lower = count_case_letters(user_input)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
