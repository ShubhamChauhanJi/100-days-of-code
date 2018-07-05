num=int(input('Enter a number to find it\'s factors:'))
#initializing a factors named list to add numbers
factors=[]
#loop to check for each number from 1 to the number itself whether it's a factor of it
for i in range(1,num+1):
    if(num%i==0):#condition to check the above
        factors.append(i)#on true add the number to the list
print(factors)
