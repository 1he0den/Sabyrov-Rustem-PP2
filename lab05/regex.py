import re

with open("row.txt", encoding="utf-8") as obj:
    data = obj.read()

print("Task number 1")
smth = re.findall(r"a.b*", data)
print(smth)

print("\n\n")

print("Task number 2")
# Task number 2
pattern2 = re.findall(r"a(bb|bbb)", data)
print(pattern2)

print("\n\n")

print("Task number 3")
pattern3 = re.findall(r"[a-z]+_[a-z]+", data)
print(pattern3)

print("\n\n")

print("Task number 4")
pattern4 = re.findall(r"[A-Z][a-z]+", data)
print(pattern4)

print("\n\n")

print("Task number 5")
pattern5 = re.findall(r"a.*b", data)
print(pattern5)

print("\n\n")

print("Task number 6")
pattern6 = re.sub(r"[ ,.]", ":", data)
print(pattern6)

print("\n\n")

print("Task number 7")
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

camel_case_str = snake_to_camel(data)
print(camel_case_str)

print("\n\n")

print("Task number 8")
pattern8 = re.split(r"(?=[A-Z])", data)
print(pattern8)

print("\n\n")

print("Task number 9")
pattern9 = re.sub(r"(?<!^)(?=[A-Z])", " ", data)
print(pattern9)

print("\n\n")

print("Task number 10")
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

snake_case_str = camel_to_snake(data)
print(snake_case_str)