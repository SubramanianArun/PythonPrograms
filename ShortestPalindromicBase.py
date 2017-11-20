#Import Modules
import sys
import time

#Import Modules
import sys
import time

##Defining palindrome checking function
def palindrome (number):
  endpointer = len(number)-1
  for startpointer in range(0,len(number)):
    if (number[startpointer] != number[endpointer]):
      return False
    endpointer -= 1
  return True

# Defining function to convert given number to the defined base
def base (value , n):
  new_number = {}
  iterator = 0
  while (value != 0):
    remainder = str(value % n)
    value = int(value/n)
    new_number[iterator] = remainder
    iterator += 1
  return new_number



#start = time.clock()       #Timer to measure the run time

#Initialize a dictionary
hash_map = {1:None}
n = 1000 #Enter the number upto which the palindromic base needs to be found
for iterator in range(1,n+1):
  hash_map[iterator] = None

#Build the dictionary
for value_iterator in range(1,n+1):
  for base_iterator in range(2,int(value_iterator/2)+1):     #Check until the half of the given number
    if(palindrome(base(value_iterator,base_iterator)) and hash_map[value_iterator] == None):
      hash_map[value_iterator] = base_iterator
  if(hash_map[value_iterator] == None):         #If not found, check for n-1 value
    hash_map[value_iterator] = palindrome(base(value_iterator,value_iterator-1))
#Brute Force Method
  '''for i in range(2,n):
    for j in range(1,n+1):
      if(palindrome(base(j,i)) and hash_map[j] == None):
        hash_map[j] = i'''

#Printing the hash_map
print ("decimal", "smallest base in which the number is a palindrome")
for value in hash_map:
  print(value, hash_map[value])

#Snippet to print the run time
'''elapsed = time.clock() - start
print('%.4f seconds' % elapsed)'''


#Finding the maximum base value for the palindrome
'''maximum = 0
for value_iterator in hash_map:
  if(hash_map[value_iterator] <= 40):
    counter+= 1
  if(hash_map[value_iterator] >= maximum):
    maximum = hash_map[value_iterator]'''




#start = time.clock()       #Timer to measure the run time

#Initialize a dictionary
hash_map = {1:None}
n = 1000 #Enter the number upto which the palindromic base needs to be found
for iterator in range(1,n+1):
  hash_map[iterator] = None

#Build the dictionary
for value_iterator in range(1,n+1):
  for base_iterator in range(2,int(value_iterator)+1):     #Check until the half of the given number
    if(palindrome(base(value_iterator,base_iterator)) and hash_map[value_iterator] == None):
      hash_map[value_iterator] = base_iterator
  if(hash_map[value_iterator] == None):         #If not found, check for n-1 value
    hash_map[value_iterator] = palindrome(base(value_iterator,n-1))
#Brute Force Method
  '''for i in range(2,n):
    for j in range(1,n+1):
      if(palindrome(base(j,i)) and hash_map[j] == None):
        hash_map[j] = i'''

#Printing the hash_map
print ("decimal", "smallest base in which the number is a palindrome")
for value in hash_map:
  print(value, hash_map[value])

#Snippet to print the run time
'''elapsed = time.clock() - start
print('%.4f seconds' % elapsed)'''


#Finding the maximum base value for the palindrome
'''maximum = 0
for value_iterator in hash_map:
  if(hash_map[value_iterator] <= 40):
    counter+= 1
  if(hash_map[value_iterator] >= maximum):
    maximum = hash_map[value_iterator]'''
