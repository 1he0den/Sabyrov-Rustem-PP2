import numpy as np

# 1st exercise

def fromGrammsToOuncees():
    grams = float(input("Enter the weight in grams: "))
    ounces = grams / 28.34952
    return (f"{grams} grams is {ounces} ounces")

print(fromGrammsToOuncees())



# 2nd exercise
def fromFarenheitToCelsius():
    farenheit = float(input("Enter the temperature in Farenheit: "))
    celsius = (farenheit - 32) * 5 / 9
    return (f"{farenheit} Farenheit is {celsius} Celsius")

print(fromFarenheitToCelsius())


# 3rd exercise

heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))

def howManyRabbitsAndChickens(heads, legs):
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits
    return (f"There are {chickens} chickens and {rabbits} rabbits")

print(howManyRabbitsAndChickens(heads, legs))


# 4th exercise


def PrimeNums():
    n = int(input("Enter the number: "))
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

PrimeNums()



# 5th exercise

# не понял пока


# 6th exercise

sentence = input("Enter a sentence: ")

def reverserOfSentence(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

print(reverserOfSentence(sentence))


# 7th exercise

def has33(self):
    for i in range(len(self) - 1):
        if self[i] == 3 and self[i + 1] == 3:
            return True
    return False

print(has33([1, 3, 3]))



def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        
    return False
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 0, 2, 4, 0, 0, 7]))


def sph_vol(r):
    from math import pi
    return (4/3) * pi * (r**3)
print(sph_vol(2))


def uniqueList(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i) 
    return res
print(uniqueList([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]))


def is_pal(s):
    return True if s == s[::-1] else False
print(is_pal('helleh'))
print(is_pal('hello'))


def hist(arr):
    for i in arr:
        print('*' * i)

hist([4, 9, 7])


def guessNumber():
    from random import randint
    rand = randint(1, 20)

    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
    counter = 0
    while True:
        num = int(input())
        counter += 1
        if num < rand:
            print('Your guess is too low.\nTake a guess.')
        elif num> rand:
            print('Your guess is too high.\nTake a guess.')
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break