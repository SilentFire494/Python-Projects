# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
n = input("Enter a sequence of comma-separated numbers: ")
n = n.split(",")  # split function is used to split the string into a list
print(n)
print(tuple(n))  # tuple function is used to convert the list into a tuple
