# PYTHON420 Week 1 Assignment 1
# Samuel Zakutney
# 5/31/20

import numpy as np
import matplotlib.pyplot as plt

# White Space Formatting
print('--White Space Formatting--')
print('% Adding blank spaces to code affects the oder in which the code runs. %\n')
def greet_user1():
    print('Hello!!!')
    print('Take care!')

print('Start')
greet_user1()
print('Finish\n')

def greet_user2():
    print('Hello!!!')
print('Take care!')

print('Start')
greet_user2()
print('Finish\n')

# Modules
print('--Modules--')
print('% Individual functions may be imported from seperate Python files %\n')
print('\tTwenty degrees Celsius converts to:')
import module
print('\t',module.convert_temp1(20),'degrees Fahrenheit')
print('\tSeventy degrees Fahrenheit converts to:')
print('\t',module.convert_temp2(70),'degrees Celsius\n')

# Strings
print('--Strings--')
print('% Individual or multiple characters may in series %')
a = "I'm a string!!"
print('\t',a,'\n')

# Exceptions
print('--Exceptions--')
print('% Lines of code that can anticipate certain occurrences, such as errors.')
try:
    weight = int(input('\tWeight = '))
    print(weight,'\n')
except ValueError:
    print("\tInvalid Input: Regardless of the wrong input, the code won't crash\n")

# Lists
print('--Lists--')
print('% Assigning multiple iterations into a single variable. Numerical values in square brackets. %')
list = [23,896,78,86]
print('\t',list)
print('\tThe second iteration in this list is:',list[1],'')
list.sort()
print('\tA sorted version of the list is:',list,'\n')

# Tuples
print('--Tuples--')
print('% Assigning multiple string iterations to a single variable, enclosed in rounded brackets %')
names = ('Jason','Zach','Billy','Kimberley','Tommy')
print('\t# of names in list:',len(names))
print('\tThe third name on the list is:',names[2],'\n')

# Dictionaries
print('--Dictionaries--')
print('% Assigning iterations for different categories under a common variable %')
identity = {
    'Name': 'Samuel Zakutney',
    'Address': '130 Negra Aroyllo Lane',
    'Birthday': '12/25/92'
}
print("\tThe identity's address is:",identity['Address'],'\n')

# defaultdict
from collections import defaultdict
print('--defaultdict--')
print('% Utilized for developing new keys for dictionaries %')
document = ['word','word','word','word','word']
word_count = defaultdict(int)
for word in document:
    word_count[word] += 1
print('\tHow many words are in the document?')
print('\t',word_count,'\n')

# Counters
from collections import Counter
print('--Counters--')
print('% Count and label how many of each iterations. %')
flavors = ['chocolate','vanilla','mint','chocolate','vanilla','chocolate']
word_count = Counter(flavors)
print('\tHow many of each flavors are there?')
print('\t',word_count,'\n')

# Sets
print('--Sets--')
print('% Sets reduce lists in length by determining its distinct elements %')
print('\tHow many flavors are listed?:',len(flavors))
flavors_set = set(flavors)
print('\tHow many distinct flavors are there?:',len(flavors_set))
print('\tWhat flavors are they?;',flavors_set,'\n')

# Control Flow
print('--Control Flow--')
print('% The use of loops to complete commands until conditions are met %')
for x in range(10):
    if x == 5:
        continue
    elif x == 7:
        break
    else:
        print('\t',x)
print('\n')

# Truthiness
print('--Truthiness--')
print('% Boolean to validate particular conditions as either True or False %')
print('\tHow many fingers does the human body have in total?')
input('\tAnswer: ')
boolean = input == 10
print('\t',boolean,'\n')

# Sorting
print('--Sorting--')
print('% Sorting rearranges the elements in a list from smallest to largest %')
prices = [19,65,22,456,334,75,89,1,34,654]
print('\tHere is a list of randomly assorted numbers:',prices)
prices.sort()
print('\tHere is the same list sorted:',prices,'\n')

# List Comprehensions
print('--List Comprehensions--')
print('% Utilized to generates lists with only desired values %')
squares = [x*x for x in range(10)]
print("\tLet's generate a list of squares:",squares,'\n')

# Automated Testing and Assert
print('--Automated Testing and Assert--')
print('% Validation that code is accomplishing the users desired task %')
def largest_item(a):
    return max(a)

assert largest_item([4,5,6,7]) == 7,"The largest number should be 7"
print('\n')

# Object Oriented Programming
print('--Object Oriented Programming--')
print('% Generating a class for which you can modify objects within it. Useful for cleaning up code %')
    # Let's generate a class named Dog
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
    # Let's set some attributes for a given variable of class Dog
d = Dog('Koby',45)
print("\tThe dog's name is:",d.get_name())
print("\tThe dog's age is:",d.get_age())
    # Given the last defining function, we can modify our input variable
d.set_age(4)
print("\tThe dog's new age is:",d.get_age(),'\n')

# Iterables and Generators
print('--Iterables and Generators--')
print('% Generators are useful for lazily retrieving elements from a list as well as other tasks %')
    # Let's set up a generator used to retrieve all the names from the random list
vip = ['Ash','Misty','Brock','Pikachu']
print("\tLet's see who's on the VIP list...")
for i, name in enumerate(vip):
    print(f"\tName {i} is {name}")
print('\n')

# Randomness
import random
print('--Randomness--')
print('% As straight forward as it sounds, it generates random numerical values or perform random selection %')
    # Let's determine a random winner from the VIP list and generate a random lottery amount.
winner = random.choice(vip)
lottery = random.randrange(50,80)
print("\tThe lottery winner from the VIP list is: ",winner)
print("\tThey won:",lottery,"million $\n")

# Regular Expressions
import re
print('--Regular Expressions--')
print('% Method of analyzing specific characters in text/strings %')
word = 'bhavsar'
re_examples = [
    re.search('v',word),
    not re.match('a',word)
]
assert all(re_examples)
print("\tSince there was no assertation error, both expressions were correct")
print("\t1. There is the letter 'v' in the word")
print("\t2. The word does not start with 'a'\n")

# Zip and Argument Unpacking
print('--Zip and Argument Unpacking--')
print('% Useful for merging lists together by pairing and unparing the of lists %')
time = ['1','2','3','4']
position = ['5','6','7','8']
final = [pair for pair in zip(time,position)]
list1,list2 = zip(*final)
print(final)
print(list1)
print(list2,'\n')

# args an kwargs
print('--Args and Kwargs--')
print('% Used to generate high-order functions with arbitrary input arguments %')
def magic(x,y,z):
    return x*y/z
x_y_list = [3,4]
z_dict = {'z': 9}
answer = magic(*x_y_list,**z_dict)
print('Answer: ',answer,'\n')

# Type Annotations
from typing import Tuple
print('--Type Annotations--')
print("% Providing hints to the input integers to facilitate computations which don't affect the code %")
names: Tuple[str,str,str,str,str] = ('Jason','Zach','Billy','Kimberley','Tommy')
print('\t# of names in list:',len(names))
print('\tThe third name on the list is:',names[2],'\n')

