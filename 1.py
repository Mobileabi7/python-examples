#1
'''برنامهای بنویسید که سه عدد از کاربر بگیرد و نسبت عدد اول را به دوعدد بعدی را چاپ نماید.
پاسخ های مجاز :
Bozogtar
Koochektar
Mosavi
Vasat'''

x1 = float(input ( " pleas enter a number , x1= "))
x2 = float(input ( " pleas enter a number , x2= "))
x3 = float(input ( " pleas enter a number , x3= "))

if x1 > x2 and x1 > x3 :
    print('-----------------')
    print("Bozorgtar")
elif x1 > x2 and x1 < x3 :
    print('-----------------')
    print('Vasat')
elif x1 < x2 and x1 > x3 :
    print('-----------------')
    print('Vasat')
elif x1 == x2 and x1 == x3 :
    print('-----------------')
    print("Mosavi")
else :
    print('-----------------')
    print("Koochektar")


