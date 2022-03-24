#3
'''-برنامه ای بنویسید که عدد n را از کاربر گرفته و مجموع و میانگین اعداد یک تا n را در خروجی محاسبه و چاپ کند.
'''

lst=[]
n= int(input ( 'please enter a number (integer) , n= ' ))
for i in range(1,n+1):
    lst.append(i)
sm=sum(lst[0:len(lst)])
print(lst)
print("Sum of numbers is : " ,sm)
print("Avrage is Numbers is : " , sm/n)


