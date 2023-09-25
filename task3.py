#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
  
(3 points)
"""
sortMe = {1: -2, 2: 6, 4: 0, 6: 1, 9: 2, 10: 3, 11: 0, 13: 3, 14: 4, 15: -2, 17: 0, 18: -1, 20: 3}


def sortbykeys():
  global sortMe
  myList = []
  for i in sortMe:
    myList.append(i)
  myList.sort()
  myList2 = []
  for i in myList:
    myList2.append(sortMe[i])
  return myList2
print(sortbykeys())

def values():
  global sortMe
  myList = []
  for i in sortMe:
    myList.append(i)
  myList.sort()
  myList2 = []
  for i in myList:
    myList2.append(sortMe[i])
    myList2.sort()
  return myList2
print(values())
    
  


