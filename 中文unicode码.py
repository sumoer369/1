print(ord('北'))# 21271
print(ord('京'))# 20140
print(chr(21271),chr(20140))
fp=open('note.txt','w')#w指write  打开文件note.txt
print('i love you',file=fp)#写入i love you到note.txt
fp.close()#关闭文件
