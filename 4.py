#4
'''برنامه ای بنویسید که از ورودی 10 عدد دریافت کند و مشخص کند بزرگترین عدد چند بار تکرار شده است.'''

c =1
lst =[]
for i in range (10):
    x = float(input(f" please enter a Number{c} : "))
    c = c+1
    lst.append(x)

count = 0
m = max(lst)
for i in lst :
    if i ==m:
        count = count+1

print(60*"-")
print ('Maximum Number is :', m ,"And this number repeat : ",count,'bar')
print(60*"-")

