#一、读取allen.txt文件中的数据
#1、打开文件，并指定打开方法
#f=open(r"e:\allen.txt","r",encoding="utf-8")
#2、对文件进行读取
#f.read(size):指定size,就按照size个数读取，不指定就是全部读取
#f.readline(size):不指定size，读取一行，指定size，则读取指定size字节长度的数据
#f.readlines():一次性把所以行数据读取出来，将其每行数据作为元素存储在一个列表中
#print(f.read())
#print(f.read(3))
#按行读取
#print(f.readline())  #这句运行，f指向了第二行开始
#print(f.readline(3))
#print(f.readlines())

#使用文件读取方法，实现一个控制台版本的小说阅读器
# import time
# f=open(r"e:\allen.txt","r",encoding="utf-8")
# #把内容一次性读出每行，保存到列表
# #列表遍历，延时输出
# for i in f.readlines():
#     print(i)
#     #每隔一秒刷新一行
#     time.sleep(1)
# #关闭文件对象
# f.close()


#二、往txt文件中写入数据
#打开文件的模式就是w或a
#f=open(r"e:\allen.txt","w",encoding="utf-8")
# f=open(r"e:\allen.txt","a",encoding="utf-8")
# #写入：allen老师，你好，大家好！！！
# #write(str):将指定的字符串str写入到文件中，是覆盖写入
# #writelines():参数是一个列表，把列表的元素作为行写入，如果需要换行，每个元素结尾要带\n字符
# #f.write("allen老师，你好，大家好！！！")
# lists=["allen\n","老师\n","你好\n","大家好\n","全国人民好！！\n"]
# f.writelines(lists)
# #读写完成以后，需要关闭文件对象
# f.close()

#三、with语句实现文件打开并读写
#更安全，可以帮助自动关闭文件对象
# with open(r"e:\allen.txt","r",encoding="utf-8") as f:
#     print(f.readlines())
# lists=["allen\n","老师\n","你好\n","大家好\n","全国人民好！！\n"]
# with open(r"e:\allen.txt","w",encoding="utf-8") as f:
#     print(f.writelines(lists))

