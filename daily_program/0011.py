import sys
res = []
with  open("C:/Users/陈/Desktop/新建文件夹/python 每天一个小程序/filtered_words.txt",'r') as f:
    text = f.readlines()
    
    for i in text:
        res.append(i.strip())
        print (i.strip())
    f.close()
str1 = input('what you want  to say:')

for  i in res:
    if i in str1:
        print ('freedom')
        
else:
    print (str1)

