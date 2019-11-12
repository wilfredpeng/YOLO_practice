import os
path='/Users/wilfred/Desktop/提款機照片集/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
files=os.listdir(path)
# print(files) #印出讀取到的檔名稱，用來確認自己是不是真的有讀到
# n = 0
# for i in files:
#     n = n + 1
# print("n=%s"%(n))
n=0 #設定初始值
print("oldName%d"%(n))
for i in files:
    oldname=files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
    newname="11_12_"+str(n)+'.jpg'
    print(oldname)
    print(newname)
    os.rename (os.path.join(path, oldname),os.path.join(path, newname))
    n = n + 1
