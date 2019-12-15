# Natnael Abay

# se.natnael.abay@gmail.com

# POST FIX CALCULATOR

def postfixEval(x):
    ##### this condittion is used to split the x given 
    if isinstance(x,str):
        x =x.split()
    ans = Stack()
    for i in x:
        if i.isdigit():
            ans.push(int(i))
        
        else:
            num1 = ans.pop()
            num2 = ans.pop()
            if i == "^":
                ans.push((num2)**(num1))
            elif i == '*':
                ans.push((num1)*(num2))
            elif i == '/':
                ans.push((num2)/(num1))
            elif i == '+':
                ans.push((num1)+(num2))
            elif i == '-':
                ans.append((num2)-(num1))
            else:
                continue
    return ans.peek()

### PREFIX ## CALCULATOR

#### prefix to postfix convertor
def prefixpost(num):
    if isinstance(num,str):
        num = num.split()
    return " ".join(num[::-1])


#################################CONVERSION####################################################
### you could uncomment and run it
##def infixp(l):
##    ans = []
##    operation = Stack()
##    op = ["/","*","^"]
##    for i in l:
##        if i.isdigit() or i.isalpha():
##            ans.append(i)
##        elif i == "(":
##            operation.push(i)
##        elif i == ")":
##            while True:
##                if operation.peek() == "(":
##                    break
##                ans.append(operation.pop())
##            operation.pop()
##
##        elif i == "+":
##            if operation.isempty():
##                operation.push(i)
##            else:
##                if operation.isempty() in op:
##                    while not operation.isempty():
##                        ans.append(operation.pop())
##                    operation.push(i)
##                else:
##                    operation.push(i)
##        elif i == "-":
##            if operation.isempty():
##                operation.push(i)
##            else:
##                if operation.peek() in op:
##                    while not operation.isempty():
##                        ans.append(operation.pop())
##                    operation.push(i)
##                else:
##                    operation.push(i)
##        elif i == "*":
##            if operation.isempty():
##                operation.push(i)
##            else:
##                if operation.peek() == "^":
##                    while not operation.isempty():
##                        ans.append(operation.pop())
##                    operation.push(i)
##                else:
##                    operation.push(i)
##        elif i == "/":
##            if opeartion.isempty():
##                operation.push(i)
##            else:
##                if operation[-1] == "^":
##                    while not operation.iempty():
##                        ans.append(operation.pop())
##                    operation.push(i)
##                else:
##                    operation.push(i)
##        elif i == "^":
##            operation.push(i)
##
##    if not operation.isempty():
##        while not operation.isempty():
##            ans.append(operation.pop())
##    return " ".join(ans)
######## to convert infix to prefix we just need to reverse the returned list form the above function
##def infixpre(num):
##    if isinstance(num,str):
##        num = num.split()
##    ans = infixp(num)
##    return ans[::-1]
##               
##print(infixpre("( A + B ) * ( C + D )"))
