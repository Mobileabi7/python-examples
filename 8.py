#8
'''-برنامه ای که دو لیست را گرفته، تعیین میکند که آیا آنها حداقل یک عضو مشترک دارند یا خیر؟'''


a = [1, 2, 3, 7, 5] 
b = [9, 8, 32, 65, 45]
if (set(a) & set(b)) !=set() :
    print('Ozv Moshterak vojood darad')
else :
    print('Ozv Moshterak vojood nadarad')

#print(set(a) & set(b))