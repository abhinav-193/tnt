1
# Write a python program to count the even and odd number from a series of numbers.
series = [12, 44, 16, 101, 21, 40, 45, 66, 93, 6, 11, 31,89]

even_no, odd_no = 0, 0
for i in series:
    if i % 2 == 0:
        even_no += 1

    else:
        odd_no+= 1

print("Even numbers are  : ", even_no)
print("Odd numbers are: ", odd_no)

2
# WAPP to get the Fibonacci series between 0 to 50.
fib = [1,1]
i = 0
while i < 51:
    fib.append(fib[-1]+fib[-2])
    i = fib[-1]
fib.remove(fib[-1])
print(fib)

3
# WAPP that print all the numbers between 0 to 6 except 3 and 6.
for x in range(7):
    if (x == 3 or x == 6):
        continue

    print(x, end=' ')

print("\n")

4
# WAPP those numbers which are divisible by 7 and multiple of 5 between 1500 and 2700 (both included).
for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:
        print("  ", x)

5
# WAPP that accept a word from the user and reverse it
word = input("Enter a word : ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")