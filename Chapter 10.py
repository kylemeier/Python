#10.1
def nested_sum(values):
    total = 0
    for items in values:
        for nested in items:
            total += nested
    return total

#10.2
def capitalize_nested(strings):
    res = []
    for items in strings:
        for nested in items:
            res.append(nested.capitalize())
    return res

#10.3
'''Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6].'''
def cum_sum(nums):
    total = 0
    cumsum = []
    for num in nums:
       total += num
       cumsum.append(total)
    return cumsum

#10.4
'''Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3].'''
def middle(t):
    mid = t[:]
    del mid[0]
    del mid[len(mid)-1]
    return mid

#10.5
'''Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None.'''
def chop(t):
    del t[0]
    del t[len(t)-1]

#10.6
'''Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc.'''
def is_sorted(t):
    for i in range(len(t)-1):
        
        if t[i+1] < t[i]:
          return False  

    return True

'''Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.'''
def is_anagram(s1,s2):
    t1 = list(s1)
    t2 = list(s2)
    t1.sort()
    t2.sort()
    return ''.join(t1) == ''.join(t2)

'''Exercise 10.8. The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.'''

import random

def has_duplicates(t):
    sort = t[:]
    sort.sort()
    for i in range(len(sort)-1):
        if sort[i] == sort[i+1]:
            return True

def birthday_duplicates():
    birthdays = []
    count = 0
    i = 0
    while i < 1000:
        for items in range(23):
            birthdays.append(random.randint(1,365))

        if has_duplicates(birthdays):
                count += 1
        i +=1
    return count/i * 100



'''Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. Hint: they don’t have to be in the same order.'''
def remove_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            del s[i]
    return s

'''Exercise 10.10. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?'''

import time

f = open('words.txt')

def build_list1():
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    f.seek(0)
    return word_list

def build_list2():
    word_list = []
    for line in f:
        word = line.strip()
        word_list += [word]

'''Exercise 10.11. Write a function called bisect that takes a sorted list and a target value and returns the index of
the value in the list, if it’s there, or None if it’s not.'''
import math

def bisect(words, word):
    top = 0
    bottom = len(words)
    section = 0
    mid = 0
    repeat = 0
    max_repeat = len(words)
    while True:
        mid = math.floor((top+bottom)/2)

        if word < words[mid]:
            bottom = mid
            
        elif word > words[mid]:
            top = mid
            
        else:
            print(mid)
            break
        
        repeat += 1
        if repeat > max_repeat:
            print("Not found")
            break

from bisect import bisect_left


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False
    
'''Exercise 10.12. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.'''
def search(words, word):
    top = 0
    bottom = len(words)
    section = 0
    mid = 0
    repeat = 0
    max_repeat = 20
    while True:
        mid = math.floor((top+bottom)/2)

        if word < words[mid]:
            bottom = mid
            
        elif word > words[mid]:
            top = mid
            
        else:
            return True
            break
        
        repeat += 1
        if repeat > max_repeat:
            return False
            break
        
def reverse_pair():
    words = build_list1()
    f.seek(0)
    for line in f:
        word = line.strip()
        revword = word[::-1]
        if revword != word:
            if search(words, revword):
                print(word, revword)

'''Exercise 10.13. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled.”'''
def interlock(words):
    for line in f:
        interlocked_word = line.strip()
        word1 = interlocked_word[::2]
        word2 = interlocked_word[1::2]
        if search(words, word1) and search(words, word2):
            print(interlocked_word, word1, word2)
            
'''Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?'''
def interlock_gen(words, word, n):
'''words: word list
   word: specific word from wordlist being evaluated
   n: number of interlocking words
   '''
    interlocked_word = word.strip()
        
    for i in range(n):

        word_check = interlocked_word[i::n]

        if not search(words,word_check):
            return False
            
    return True   
    




            
        
    
    

