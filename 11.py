#11
#check  n is power of 2?
'''
برنامه ای که عددی را خوانده، تعیین می کند که آیا توانی از 2 است یا خیر؟
'''
n = int(input("please enter a number (int) : "))

if n ==0 :
    print ( "no")
else :
    n_new =n/2

while n_new!= 1 :
        
    print(n_new)
    if n_new % 2 != 0 :
        print("No")
        
    elif n_new*n_new == n :
        print("yes")
           

