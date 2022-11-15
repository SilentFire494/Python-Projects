# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
n = int(input("What number do you want to input? "))
d = dict()
for i in range(1, n + 1):  # range function is used to generate a sequence of numbers
    d[i] = i * i  # d[i] is the key and i * i is the value
    print(d)
