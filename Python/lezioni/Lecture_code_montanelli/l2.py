import sys

# string manipulation

s = "STEfano montanelli"

# basic built-in functions
print(s.capitalize())   # Stefano montanelli, function that capitalize the first letter of the string
print(s.title())        # Stefano Montanelli, function that capitalize the first letter of each word
print(s.lower())        # stefano montanelli, function that _lower_ the case of each letter in the string
print(s.upper())        # STEFANO MONTANELLI, function that _upper_ the case of each letter in the string
print(s.swapcase())     # stEFANO MONTANELLI, function that swap the case of each letter in the string (lower to upper and viceversa)


"""
    you can work with a string as you work with lists. By definition in Python a string is seen as a list: 
    every character in the string is seen as an element of a list.
"""
# string slicing (through list slicing), the same concept is applied to lists, tuples, dictionaries, etc.
"""

        [start:stop:step]

"""
s = "STEfano montanelli"

print("result of S[0]: ", s[0])                 # S, first element of the string
print("result of s[1:4]: ", s[1:4])             # TEf, from the second to the fourth element of the string
print("result of s[-1]: ", s[-1])               # i, last element of the string
print("result of s[-4:-1]: ", s[-4:-1])         # ell, from the fourth to the second element of the string
print("result of s[-1:-4]: ", s[-1:-4])         # empty string, the step is positive and the start is greater than the stop, NOT ERROR
print("result of s[1:]", s[1:])                 # TEfano montanelli, from the second element to the end of the string    
print("result of s[:-1]", s[:-1])               # STEfano montanell, from the first element to the second last element of the string
print("result of s[-5:]", s[-5:])               # nelli, from the fifth last element to the end of the string
print("result of s[:-5]", s[:-5])               # STEfano monta, from the first element to the fifth last element of the string    
print("result of s[5:]", s[5:])                 # no montanelli, from the sixth element to the end of the string
print("result of s[:5]", s[:5])                 # STEfa, from the first element to the fifth element of the string
print("result of s[1:4:2]: ", s[1:4:2])         # Tf, from the second to the fourth element of the string with step 2
                                                # it prints from 1 up to 4, taking every 2 character, so the 1st and the 3rd
"""     slicing by an interval like [1:4] means that we are not considering the 4th element of the string
            but we are considering the 1st, 2nd and 3rd element of the string NOT INCLUDING THE 4
"""

print("result of s[1:4]: ", s[1:4])             # TEf, from the second to the fourth element of the string, EXCLUDED THE 4th
print("result of s[::2]: ", s[::2])             # Sfno onal, from the first to the last element of the string with step 2 (even elements)
print("result of s[1::2]: ", s[1::2])           # Tenoatnli, from the second to the last element of the string with step 2 (odd elements)
print("result of s[-6:-2]: ", s[-6:-2])         # ntel, from the sixth last to the second last element of the string
print("result of s[-6:-2:-2]: ", s[-6:-2:-2])   # empty string, the step is negative and the start is greater than the stop, NOT ERROR
print("result of s[::-1]: ", s[::-1])           # illenatnom onafETS, from the last to the first element of the string with step -1 (reversed string)



# given a string in input, return true/false if it is a palindrome (case insensitive)
# radar, otto, civic


def check_pal(w):
    """check if a word in input is palindrome.

    Keyword arguments:
    string -- the word to evaluate

    Return:
    bool -- True when palindrome; False otherwise
    """
    w = w.lower() # convert the string to lower case
    rw = w[::-1]

    # as an alternative to the if statement:
    # return w == rw
    if w == rw:
        return True
    else:
        return False

"""let's change this function and the algorith beyond it in order not to slice the string, but using a diffetent approach"""

def check_pal_iteration(w):
    """check if a word in input is palindrome through iteration.

    Keyword arguments:
    string -- the word to evaluate

    Return:
    bool -- True when palindrome; False otherwise
    """
    left = 0
    right = len(w) - 1
    is_pal = True

    while left < right:
        if w[left].lower() != w[right].lower():
            is_pal = False
            # break stops the while and goes to the next operation after the loop
            break

        left += 1
        right -= 1

    return is_pal 


# main code
word = "abcd45dcba"

if check_pal_iteration(word):
    # have a look at the print function in Python:
    # https://docs.python.org/3/tutorial/inputoutput.html
    print(f"the '{word}' is palindrome")
else:
    print(f"the '{word}' is not palindrome")

sys.exit()

# more exercises on string manipulations:
# https://www.geeksforgeeks.org/python-string-exercise/
# use a serch engine for more
