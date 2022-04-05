#12
'''
برنامه ای بنویسید که تعداد حروف الفبا را خوانده و الگوی نظیر خروجی زیر را نمایش می دهد
(n=4)
     A
   A B A
  A B C B A
A B C D C B A

'''
# my_list = ['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


n = int(input('Please Enter a Number (int) : '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()


