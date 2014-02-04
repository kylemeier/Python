#8.2
prefixes = 'JKLMNOPQ'
suffix = 'ack'

'''for letter in prefixes:
    if letter == "O" or letter == "Q":
        print (letter + "u" + suffix)
    else:
        print (letter + suffix)'''

#8.3
fruit = 'fruit'

#8.4
def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return - 1

#8.5
def count(string, letter):
    counter  = 0
    for i in string:
        if i == letter:
            counter = counter + 1
    return counter

#8.6
def count2(word,letter):
    counter = -1
    index = 0
    while index < len(word)-1:
        find(word,letter,index)
        counter = counter + 1
        index = index + 1
    return counter

#8.7
word = 'banana'

#8.10
def is_palindrome(word):
    return(word == word[::-1])

#8.11
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#checks if first letter is lowercase       
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#checks if 'c' is lowercase, will always be true

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
#checks if last letter in string is lowercase

    
def any_lowercase4(s):
    flag = False
    for c in s:
        
        flag = flag or c.islower()
    return flag

#stays true if switched to true, works

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#checks if first letter isn't lowercase

#8.12
import string

def rot_letter(letter, amount):
    
    if letter.isupper():
        start = ord('A')
            
    elif letter.islower():
        start = ord('a')

    else:
        return letter
        
#get distance
    distance = ord(letter) - start

#use distance from start and rotation amount to get new distance from start
    new_distance = (distance + amount) % 26 + start
    return chr(new_distance)



def rot_word(word, amount):
    rot = ""
    for i in word:
        l = rot_letter(i,amount)
        rot = rot + l

    return rot

        

    


        


    
        

