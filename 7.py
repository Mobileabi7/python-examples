#7
# for runing program you should install package cur by pip install cur
'''برنامه ای که نام فایلی را خوانده، تعیین کند که آیا این فایل از نوع GIF است یا خیر؟
راهنمایی : ) فایلی با نوع GIF است که بایتهای اول تا چهارم آن" GIF8 "باشند ('''


def write_file(data, filename): 
    with open(filename, 'wb') as f: 
        f.write(data)
        
firstRow = cur.fetchone() 
write_file(firstRow[0].read(), "blah.zip")
