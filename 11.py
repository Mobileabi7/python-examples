#11
n = int(input("please enter a number (int) : "))

if n ==0 :
    print ( "no")
else :
    while n!= 1 :
        n =n/2
        if n==1:
            print ("yes")
        elif n< 1 :
            break
    print ("No")

