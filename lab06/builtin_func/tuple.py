def all_elements_true(tup):
    return all(tup) 

tup = tuple(map(int, input("Enter tuple elements separated by spaces (0 for False, any other number for True): ").split()))

result = all_elements_true(tup)

print("All elements are True:", result)