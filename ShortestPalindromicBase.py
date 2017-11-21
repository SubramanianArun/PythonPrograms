#Import Modules
import sys
import time

#Define input validation function
def validate_input (number) :
    if number is None:
        return None
    elif type(number) == type(0):
        number = [int(convert) for convert in str(number)] #If it is an integer, convert it into an integer array
        return number
    elif type(number) == type({}):
        if type(number[0]) == type(0): #Check if Hashmap values have integer key values or else discard input
            return number
        else :
            return None
    else :                   #Discard all other data type inputs
        return None

##Defining palindrome checking function
def palindrome (number):
  number = validate_input(number)   #Call validating function
  if number != None :               #Execute if the input is valid
      endpointer = len(number)-1
      for startpointer in range(0,len(number)):
        if (number[startpointer] != number[endpointer]):    #Compare from first and last indices and move to the center
          return False
        endpointer -= 1
      return True

# Defining function to convert given number to the defined base
def base (value , n):
  new_number = {}       #Initiate dictionary for the number output
  iterator = 0
  if n <= 1 or value <= 0 or isinstance(value, float) or isinstance(n , float): #Discard incorrect values or types
    return None
  else:
    while (value != 0):                         #Extract digit by digit from the number and store it in a dictionary
        remainder = int(value % n)
        value = int(value/n)
        new_number[iterator] = remainder
        iterator += 1
    return new_number

###################################################################################
##      Return the number to the required base in the form of a dictionary       ##
##      because as we convert numbers beyond a point we might run out of symbols ##
##      to represent values. Hence, we might get a remainder value in multiple   ##
##      digits. For example, 33 base 32 should be 11. But if we keep it as       ##
##      numbers/string data type we might get it as 132                          ##
###################################################################################


start = time.clock()       #Timer to measure the run time

#Initialize a dictionary
hash_map = {1:None}
n = 1000 #Enter the number upto which the palindromic base needs to be found
for iterator in range(1,n+1):
  hash_map[iterator] = None

#Build the dictionary
inner_loop_iterator = 0
for value_iterator in range(1,n+1):
  if (value_iterator < 10): #Handling edge cases for numbers less than 10
      inner_loop_iterator = 10
  else:
      inner_loop_iterator = int(value_iterator/2)
  for base_iterator in range(2,inner_loop_iterator+1):     #Check until the half of the given number
    if(palindrome(base(value_iterator,base_iterator)) and hash_map[value_iterator] == None):
      hash_map[value_iterator] = base_iterator
  if(hash_map[value_iterator] == None):   #If not found, assign n-1 value
    hash_map[value_iterator] = value_iterator-1

#Brute Force Method
  '''for i in range(2,n):
        for j in range(1,n+1):
            if(palindrome(base(j,i)) and hash_map[j] == None):
                hash_map[j] = i'''

#Printing the hash_map
print "decimal", "smallest base in which the number is a palindrome"
for value in hash_map:
  print value, hash_map[value]

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
