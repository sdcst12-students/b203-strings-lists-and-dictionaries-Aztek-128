#!python3
"""
Have the user enter an integer value 'n'
write a python script to use all of the integers from 1 to n as the keys and the squares of those numbers as the values (2 points)
sample result:
x = { 1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64, 9 : 81, 10 : 100 }
"""

n = int(input("enter in a value:  "))
vocab = {}
for i in range(n+1):
    number = i ** 2
    vocab[i] = number
print(vocab)