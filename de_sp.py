#-*- coding:utf8-*-
#删除关系中的空白行
import codecs
#/Users/kun/Desktop/
infopen = codecs.open(r"C://2007//4_2_2", "r", "utf-8")
outfopen = open(r"C://2007//4_2_2_2","a+",encoding='utf-8')

#infopen = open(r"D://555_2",'r')
#outfopen = open(r"D://555_3",'w')
lines = infopen.readlines()
for line in lines:
    if line.split():
        outfopen.writelines(line)
    else:
        outfopen.writelines("")
infopen.close()
outfopen.close()
