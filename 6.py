#6
'''-برنامه ای که یک فایل و عدد n را خوانده، سپس n سطر انتهای فایل را نمایش بدهد.
'''
#test git
n = int(input('Please Enter a number (integer):' ))
file1 = open('myfile.txt', 'r')
lines = file1.readlines()
l = len(lines)
c = 0
if n> l :
    print("addad vared shodeh bishtar az sotoor hast")
else:
    while c < n :
        print ( lines[-1-c])
        c = c+1
