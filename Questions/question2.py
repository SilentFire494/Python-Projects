# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
# In case of input data being supplied to the question, it should be assumed to be a console input.
number = input("What number do you want to find the factorial of? ")
number = int(number)
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
    print(factorial)
