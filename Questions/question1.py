# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
n = []

for n in range(2000, 3201):  # range function is used to generate a sequence of numbers
    if (n % 7 == 0) and (n % 5 != 0):  # if statement is used to check the condition
        print(n, end=",")  # print function is used to print the output
