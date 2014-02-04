f = open('words.txt')

#9.1
def printwords():
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word)

#9.2
def has_no_e(word):
        if word.find('e') == -1:
            return True
        
    
def no_e_percentage():
    total = 0
    noe = 0
    for line in f:
        word = line.strip()
        if has_no_e(word):
            noe = noe+1
        total = total+1
    percentage = noe/total * 100


#9.3
          
def best_letter():
    total = 0
    bestletter = ''
    bestletters = [0,0,0,0,0]
    besttotals = [0,0,0,0,0]    
    i = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    for letter in alphabet:
        total = avoids(letter)
        for value in besttotals:
            if total > value:
                besttotals.append(total)
                besttotals.remove(value)
                bestletters.append(letter)
                bestletters.remove(bestletters[i])
                break
            i = i+1
        i = 0
            
                    
            
    print(bestletters)
   

def avoids(letter):
    atotal = 0
    for word in f:
        strippedword = word.lstrip(letter)
        if len(strippedword) == len(word):
            atotal = atotal+1
    f.seek(0)
    return atotal


#9.4
def uses_only(word,string):
    for letter in word:
        if string.find(letter) == -1:
            return False
    return True

def sentence():
    for line in f:
        word = line.strip()
        if uses_only(word,'acefhlo'):
            print(word)

#9.5
def uses_all(word,string):
    for letter in string:
        if word.find(letter) == -1:
            return False
    return True

def exercise95():
    total = 0
    for line in f:
        word = line.strip()
        if uses_all(word,'aeiou'):
            total = total+1
    print(total)



#9.6  
def abcedarian_check(word):
    i = 1
    for letter in word:
        if i < len(word):
            if ord(letter) > ord(word[i]):
                return False
        i = i+1
    return True
   
def exercise96():
    count = 0
    for line in f:
        word = line.strip()
        if abcedarian_check(word):
            count = count+1
    print(count)


#9.7
def exercise97():
    for line in f:
        word = line.strip()
        if double_check(word):
            return word

def double_check(word):

    amount_of_doubles = 0
    i = 0
    
    while i < len(word)-1:
        #print(word[i],word[i+1])
        if word[i] == word[i+1]:
            amount_of_doubles = amount_of_doubles + 1
            i = i+2
        else:
            amount_of_doubles = 0
            i = i+1
           
        #print(consecutive_letters, amount_of_doubles)
            
            
        if amount_of_doubles >= 3:
            return True

  
#9.8            

    
def palindromes():
    number = 0
    checknumbers = ''
    while number < 999999:
        number = number+1
        padded_number = convert_number(number)
        checknumber = padded_number[2:]
        if palindrome_check(checknumber):
            padded_number = convert_number(number+1)
            checknumber = padded_number[1:]
            if palindrome_check(checknumber):
                padded_number = convert_number(number+2)
                checknumber = padded_number[1:5]
                if palindrome_check(checknumber):
                    padded_number = convert_number(number+3)
                    if palindrome_check(padded_number):
                        print(number)


def convert_number(number):
    padded_number = number
    padded_number = str(padded_number)
    while len(padded_number) < 6:
        padded_number = "0"+padded_number
    return padded_number

def palindrome_check(string):
        return string == string[::-1]
        
        
#9.9
#take an age, reverse it, find the difference
#increment age by 1 and add the difference, check if it's the reverse
#go until 99, if it's matched 8 times, print the sixth time

def age_difference(age):
    mom_age = ''
    age = str(age)
    age = age.zfill(2)
    mom_age = age[::-1]   
    difference = int(mom_age) - int(age)
    return difference

def check_reverse(age, difference):
    mom_age = age+difference
    mom_age = str(mom_age)
    age = str(age)
    age = age.zfill(2)
    return mom_age == age[::-1]

def increment_ages():
    returned_age = 0
    for age in range(1,100):
        ages_array = []
        difference = age_difference(age)
        if difference > 0:
            for agecheck in range(age,100):
                if check_reverse(agecheck,difference):
                    ages_array.append(agecheck)
        
            if len(ages_array) == 8:
                print(ages_array[5])




def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print (daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print (diff, n)
        diff = diff + 1

#print ('diff  #instances')
#check_diffs()

#print()
#print ('daughter  mother')
#num_instances(18, True)


  

   
    



    



    





        

    


        



