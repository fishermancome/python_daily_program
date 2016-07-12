import sys

def load_filtered_words(file):
    words = []
    with open(file,'r') as f:
        content = f.readlines()
        for line in content:
            words.append(line.strip())
        f.close()
    return words

def replace_sensitve_words(words):
    str1 = input("enter what you want to input:")
    for i in words:
        if i in str1:
            
            str1 = str1.replace(i,'*'*len(i))
            print (str1)
            sys.exit()
    else:
        print (str1)

if __name__ =="__main__":
    file = 'C:/Users/陈/Desktop/新建文件夹/python 每天一个小程序/filtered_words.txt'
    replace_sensitve_words(load_filtered_words(file))
