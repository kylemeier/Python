'''Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary'''
f = open('words.txt')

def create_word_dict():
    word_dict = dict()
    for line in f:
        word = line.strip()
        word_dict[word] = word
    return word_dict


'''Exercise 11.2. Use get to write histogram more concisely. You should be able to eliminate the if statement.

def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d'''

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

'''Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.

def print_hist(h):
for c in h:
print c, h[c]'''

def print_hist(h):
    key_list = sorted(h.keys())
    for key in key_list:
        print(key, h.get(key)) 

'''Exercise 11.4. Modify reverse_lookup so that it builds and returns a list of all keys that map to
v, or an empty list if there are none.

def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise ValueError'''

def reverse_lookup(d, v):
    list_of_matches = []
    for k in d:
        if d[k] == v:
            list_of_matches.append(k)
    return list_of_matches

'''Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

'''
def invert_dict(dic):
    inverse = {}
    for key, val in dic.items():
        inverse.setdefault(val, []).append(key)
    return inverse

'''Exercise 11.7. Memoize the Ackermann function from Exercise 6.5 and see if memoization
makes it possible to evaluate the function with bigger arguments.'''
known_m = {}
known_n = {}
def A(m,n):
    if m in known_m and n in known_n:
            return 

    
    if m == 0:
        return n+1
        
    if n == 0:
        return A(m-1,1)

    return A(m-1, A(m,n-1))

    

