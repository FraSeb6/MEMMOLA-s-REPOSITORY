
#sttring manipulation
s= 'stefano montaneli'
w='radar'
#rw= w[-1:0:-1]
rw= w[::-1]

#basic built-in functions
print(s.capitalize())
print(s.lower())
print(s.upper())

#string 
print(s[0]) #only first element S
print("result of print(s[1:4])",s[1:4])#
print(s[-1])
print(s[1:])
print(s[:1])
print(s[:-1])
print("result of print(s[-1:-4])",s[-1:-4])#not sintatical incorrect but it dosen't give a result
print("result of print(s[:5])",s[:5])
print("result of print(s[-5:])",s[-5:])
print("result of print(s[5:])",s[5:])
print("result of print(s[:-5])",s[:-5])
print("result of print(s[1:4])",s[1:4])
print("result of print(s[1:4:2])",s[1:4:2])#skippa la cella 2
print("result of print(s[::2])",s[::2]) #returns odd elements in the string [not in the index]
print("result of print(s[-3:-6])",s[-3:-6])
print("result of print(s[-3:-6:-2])",s[-3:-6:-2])


print(s[0].upper()+s[1:])
print("result of s[1:4]", s[1:4].lower())


if w==rw:
    print("they are palindrome")
else:
    print("they are not palindrome")
    
#since checking palindrome is a sort of function , I define a targeted specification
def check_pal(w):
    w=w.lower()
    rw=w[::-1]
    if w==rw:
        return True
    else: 
        return False    
    
def sheck_pal_iteration(w):
    left=0
    right= len(w)-1
    is_pal = True
    while left < right:
        if w[left] !=w[right]:
            is_pal= True
            #stop
            break
        left += 1
        right -=1
    return is_pal