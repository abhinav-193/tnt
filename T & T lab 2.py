# 1
str = input("Enter a string\n")
modified_string = str[::2]
print(modified_string)
# 2

n_terms = int(input("How many terms? "))

# first 2 terms
n1, n2 = 0, 1
count = 0


if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence upto", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
#3
import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0   # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print(" you lost: try again")
        print("Please guess higher ")
    elif guess > answer:  # guess must be greater than number
        print(" you lost:  try again")
        print("Please guess lower ")
    else:
        print("you are winner")

#4
def CheckLeap(Year):

    if((Year % 400 == 0) or
            (Year % 100 != 0) and
            (Year % 4 == 0)):
        print("Given Year is a leap Year");

    else:
        print ("Given Year is not a leap Year")

Year = int(input("Enter the number: "))
CheckLeap(Year)
#5
n = input("Enter number between 1 to 6")
print(len())

#6
for x in range(1, 101):
    prime = True
    for i in range(2, x):
        if (x % i == 0):
            prime = False
    if prime == True:
        print(x)
