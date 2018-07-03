num1=input("enter the first number:")
num2=input("enter the secound number:")
ch=input('enter the operation symbol(+,-,*,/)')
def calc(var,p,q):
    switcher = {
        '+': p+q,
        '-': p-q,
        '*': p*q,
        '/':p/q
             }
    return switcher.get(var,"Invalid choice")
print('the output is: '+ str(calc(str(ch),int(num1),int(num2))))
    
