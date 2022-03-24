#2
'''برنامه ای بنویسید که نمرات دانش آموزان یک کالس بیست نفره را بگیرد و شماره بیشترین نمره را چاپ کند به طور
مثال اگر سومین نمره بیسترین بود عدد 3 را چاپ کند)جایگاه نمره چاپ شود(
    '''
c =1
lst =[]
for i in range (20):
    x = float(input(f" please enter Score for Students {c} : "))
    c = c+1
    lst.append(x)

print(25*'-')
print(lst)
print(25*'-')
print("index of maximum Score is : ",(lst.index(max(lst))+1))
print(25*'-')

