import re
from collections import Counter
filepath = 'C:/Users/陈/Desktop/新建文件夹/words.txt'
pattern = r'''[A-Za-z0-9]+'''
with open(filepath,'r') as f:
    r = re.findall(pattern,f.read())
    
    count = len(r)
    print('一共有%d个单词'%count)
    print(Counter(r).most_common())


