#2
size = 10
string = '*'
for i in range(1,size + 1):
     
     if i< size:
         print(" "*(size-i),end= "")
     print(string)
     string += "**"
