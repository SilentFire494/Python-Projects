# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# map function is used to map the values to the specified function
x, y = map(int, input().split(","))
list = []

for i in range(x):  # range function is used to generate a sequence of numbers
    list.append([])  # append function is used to add an element to the list
    for j in range(y):
        list[i].append(i*j)
print(list)  # print function is used to print the output
