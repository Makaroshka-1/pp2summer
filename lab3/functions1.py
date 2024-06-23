import math
import random

def g_to_oz(grams):
    return 28.3495231 * grams

def F_to_C(farenheit):
    return (5 / 9) * (farenheit - 32)

def solve_puzzle(head, legs):
    for c in range(head + 1):
        r = head - c
        if 2*c+4*r == legs:
            return c,r
    return None, None

def filter_prime(nums):
    primes = [] 
    for i in range(len(nums)):
        for j in range(2,nums[i//2+1]):
            if nums[i]%j==0:
                break
            else:
                primes.append(nums[i])
                break
    return primes

def permute(string, step = 0):
    if step == len(string):
        print("".join(string))
    else:
        for i in range(step, len(string)):
            string_copy = [c for c in string]
            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            
            permute(string_copy, step + 1)  

def reverse(string):
    string = string.split(' ')
    string = string[::-1]
    string = ' '.join(string)
    return string

def has_33(nums):
    for i in range(1,len(nums)-1):
        if nums[i] == 3 and (nums[i+1]==3 or nums[i-1]==3):
            return True
    return False

def spy(nums):
    for i in range(1,len(nums)-1):
        if nums[i]==0 and nums[i-1]==0 and nums[i+1]==7:
            return True
    return False

def sphere_volume(R):
    return 4/3*math.pi*R**3

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
            
def palindrome(string):
    if string == string[::-1]:
        return True
    return False

def histogram(nums):
    for i in range(len(nums)):
        print("*"*nums[i])

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    guesses_num = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_num += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_num} guesses!")
            break

        
