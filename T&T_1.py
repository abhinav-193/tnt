
mark = []                                                                   #1st
tot = 0
print("Enter marks Obtained : ")
for i in range(5):
    mark.insert(i, float(input()))

for i in range(5):
    tot = tot + float(mark[i])
avg = tot/5
CGPA = avg/9
if avg>=91 and avg<=100:
    print("Your Grade is O")
    print("your CGPA is {:.2f}".format(CGPA))
elif avg>=81 and avg<91:
    print("Your Grade is E")
    print("your CGPA is {:.2f}".format(CGPA))
elif avg>=71 and avg<81:
    print("Your Grade is A")
    print("your CGPA is {:.2f}".format(CGPA))
elif avg>=61 and avg<71:
    print("Your Grade is B")
    print("your CGPA is {:.2f}".format(CGPA))

else:
    print("You are fail")

string = "My name is Shubham";                                          #2nd
count = 0;

for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1;
print("Total number of characters in a string: " + str(count));

def find_longest_word(words_list):                                     #3rd
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Shubham", "love", "cat"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

old_str = "Helloo World"                                                #4th
n = int(input("Enter the index "))
mod_str = ''
for char in range(0, len(old_str)):

    # char index is equivalent to n
    if(char != n):
        # append original string character
        mod_str += old_str[char]

print("Modified string after removing ", n, "th character ")
print(mod_str)



old_str = input("Enter a string : ")                                          #5th
new_str = old_str[-1:] + old_str[1:-1] + old_str[:1]
print(new_str)

output_string = ""                                                           #6th

oddOrEven = int(input("Enter '1' to remove even char:"))

if oddOrEven == 1 :
    print ("String after removing characters on even position : ")
    for i in range(len(input_string)):
        if i%2 == 0:
            output_string = output_string + input_string[i]

print (output_string)

user_input = input("Enter your name")                                        #7th
print("name in upper case ", user_input.upper())
print("name in lower case ", user_input.lower())

my_str = 'dad'                                                                #8th

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")