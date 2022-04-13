#!/usr/bin/env python
# coding: utf-8

# # Python Function Exercises
# 
# 
# 
# ### 1) Define a function named is_two. 
# #### It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[51]:


#function will accept string form or digit form of 2 and return True or False

def is_two(n):
    #check that the submission is equal to 'two' or 2
    if n == 'two' or n == '2' or n == 2:
        #create a boolean return
        return True
    else:
        return False


# In[123]:


# In[124]:


## class example:

def is_two(n):
    return n == 2 or n == '2'


# In[125]:


# ### 2) Define a function named is_vowel. 
# #### It should return True if the passed string is a vowel, False otherwise

# In[61]:


# is_vowel check that is a passed letter is a vowel or not

def is_vowel(strg):
    #set up a list where letter (aka strg) can be compared to lower and upper case vowels
    if strg in ['A','a','E','e','I','i','O','o','U','u']:
        #set up return to be boolean
        return True
    else:
        return False


# In[60]:


# In[126]:


## class example:

def is_vowel(somestring):
    if type(somestring) == str:
        result = somestring.lower()in ['a','e','i','o','u']
        return result
    else:
        False


# In[132]:


# ### 3) Define a function named is_consonant. 
# #### It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[62]:


#is_consonant sees if passed letter is a consonant or not, using the function is_vowel

def is_consonant(strg):
    #we use the function is_vowel to simplify this process (and not write out all consonants)
    if is_vowel(strg):
        #set up return as boolean values
        return False
    else:
        return True
        


# In[83]:


# In[136]:


#class example:

def is_consonant(somestring):
    if type(somestring)== str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel(somestring)
    return False


# In[138]:


# ### 4) Define a function that accepts a string that is a word. 
# #### The function should capitalize the first letter of the word if the word starts with a consonant.

# In[70]:


#cap_letter will capitilize the passed string ONLY if it begins with a consonant, using function is_consonant

def cap_letter(message):
    #conditions are set so that our string (aka message) checks if the first letter (position[0]) meets is_consonant
    if is_consonant(message[0]):
        #using the capitalize method to caps the first letter of string
        return message.capitalize()


# In[109]:


# In[140]:


#class example:

def cap_letter(string):
    if type(string)!= str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# In[144]:


# ### 5) Define a function named calculate_tip. 
# #### It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[85]:


#calculate_tip takes in the tip percentage and bill total to determine the amount to tip

def calculate_tip(tip, total):
    #using the bill total mulitplied by the tip % to show the amount of tip needed to be paid
    return total * tip


# In[86]:


# In[146]:


#class example:

def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage mus be between 0 and 1'
    return tip_percentage * bill


# In[147]:


# ### 6) Define a function named apply_discount. 
# #### It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[87]:


#apply_discount takes in the original price of an object and the discount % to determine the total amount paid after discount

def apply_discount(og_price, discount):
    #we first get the discounted price by subtracting the discount % from one, then multiply this percentage to og price
    return og_price * (1- discount)


# In[88]:


# ### 7) Define a function named handle_commas. 
# #### It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[91]:


#handle_commas will replace any submitted number that holds a comma, and return number sans commas

def handle_commas(number):
    #we use the replace method to find any commas and replace with ''
    number = number.replace(',', '')
    return number
    


# In[92]:

# ### 8) Define a function named get_letter_grade. 
# #### It should accept a number and return the letter grade associated with that number (A-F).

# In[157]:


#get_letter_grade will accept a number and then return the letter grade associated with the number

def get_letter_grade(num):
    
    #using if and else conditions, we create groups of what number grade range will equal in letter grade terms
    
    if type(num) == int or type(num)== float:
        
        if num>87 and num<101:
            print('A')

        elif num>79 and num<88:
            print('B') 

        elif num>66 and num<80:
            print('C')

        elif num>59 and num<67:
            print('D')
        
        elif num>=0 and num<60:
            print('F')

    else:
        print('Please print your grade as a number.')
    

    


# In[96]:



# ### 9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[74]:


#remove_vowels will take in a words/string 

def remove_vowels(words):
    vowels = ["a","e","i","o","u"]
    result = [word for word in words if word.lower() not in vowels]
    result = ''.join(result)
    return(result)
    


# In[75]:


# ### 10) Define a function named normalize_name. 
# #### It should accept a string and return a valid python identifier, that is:
# ##### -anything that is not a valid python identifier should be removed
# ##### -leading and trailing whitespace should be removed
# ##### -everything should be lowercase
# ##### -spaces should be replaced with underscores

# In[80]:


def normalize_name(name):
    ###add in deletion of symbols
    submit=(name)
    return name.lower().strip().replace(' ','_')


# In[81]:


# ### 11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

# In[46]:


def cumulative_sum(num1, num2, num3):
    csum= [num1, num1 + num2, num1 + num2 + num3]
    return csum


# In[47]:


# ### BONUS ROUND:
# ### 1) Create a function named twelveto24. 
# #### It should accept a string in the format 10:45am or 4:30pm 
# #### and return a string that is the representation of the time in a 24-hour format. 
# ##### **Bonus write a function that does the opposite.

# In[120]:


# found via stackover flow
#look up "slicing syntax"

#finding a 24-hour format with submission of (HH:MM:SSPM/AM)
a=''
def twelveto24(s):
    if s[-2:] == "AM" :
        if s[:2] == '12':
            a = str('00' + s[2:8])
    else:
            a = s[:-2]
        
    if s[:2] == '12':
            a = s[:-2]
    else:
            a = str(int(s[:2]) + 12) + s[2:8]
    return a




# In[122]:



# In[ ]:


# slicing example
string = 'banana'

