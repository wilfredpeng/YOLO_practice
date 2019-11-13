import os
import re
import sys
src='/Users/*****/Desktop/'
path='/Users/*****/Desktop/'
if __name__=='__main__':
    print(len(sys.argv))
    src=src+sys.argv[1]+'/'
    print(src)
    filedir=os.listdir(src)
    print(filedir)
    f = open(src+'train.txt','w+')
    for i in filedir:
        print(path+i)
            #f.write(dst+i+'\n')
        f.write(path+i+'\n')
            #f.write((i).replace('.jpg','') + '\n')
    f.close()
