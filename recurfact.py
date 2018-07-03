num=int(input('enter a number to calculate factorical:'))
def fact(a):
   if(a>0)
     return (a*fact(a-1))
else:
    return 1
print(fact(num))
