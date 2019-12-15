# Natnael Abay

# se.natnael.abay@gmail.com
import random
def truth(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s[i].isalpha() and s[i+1].isalpha():
            return False
    return True
    
def ch1(s):
    a = ["a","c","b"]
    for i in range(len(a)):
        if s!= a[i]:
            return a[i]
def  ch2(s,b):
    a = ["a","b","c"]
    for i in a:
        if i != s and i != b:
            return i
def ch(s):
    
    a = ["a","b","c"]
    j = [char for char in s]
    if len(s)==1 and s[0] == '?':
        return 'a'
    elif len(s) == 1:
        return s
    tr = truth(s)
    if tr:
        if len(s) == 2:
            
            if j[0] == "?" and j[1]== "?":
                j[0] = "b"
                j[1] = ch1(s[0])
                return j
            elif j[0] == "?" and j[1].isalpha():
                j[0] = ch1(s[1])
                return j
            elif s[1] =="?":
                j[1] = ch1(s[0])
                return j
   
        for i in range(len(j)-1):
            if j[i] == "?" and j ==0  and len(j)>=i+1:
                if j[i+1].isalpha():
                    j[i] = ch1(j[i+1])
                else:
                    j[i+1] = s[random.randint(0,2)]
            elif j[i] == "?" and j != 0 and len(j) >= i+1:
                if j[i+1].isalpha():
                    j[i] = ch2(j[i-1],j[i+1])
                else:
                    j[i] = ch1(j[i-1])
        if j[-1] == "?":
            j[-1] = ch1(j[-2])
        return j
    else:
        return -1
size = eval(input())
c = []
for i in range(size):
    b = input()
    c.append(b)
for i in range(size):
    a = ch(c[i])
    if a == -1:
        print(-1)
    else:
        print("".join(a))
    
            
 
