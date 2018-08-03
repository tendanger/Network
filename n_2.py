#-*- coding:utf8-*-
#读入数据，将多列关系转为2列关系，并添加权重
import codecs
#/Users/kun/Desktop/
f = codecs.open(r"D://555", "r", "utf-8")

# text = f.read()
# length = len(text.splitlines())
#
# content = f.readlines()
# for i in range(1, length+1):
#     content = f.readline()
#     print(content)

line = f.readline()             # 调用文件的 readline()方法
# print(type(line))
# print(len(line))
# for i in range(len(line)):
#     print(line[i], end = '')
# print(line[0])
# #print(line[1])
# print(line[2])
# #print(line[3])
# print(line[4])
# #print(line[5])
# print(line[6])
# #print(line[7])
# #print(line[8])
# print("------")

line = line[0] +" "+ line[2] +" "+ line[6]
print(line)
line = ""
line = line[0] +" "+ line[4] +" "+ line[6]
print(line)
line = line[2] +" "+ line[4] +" "+ line[6]
print(line)


while line:
    #if len(line)
    #print line,                 # 后面跟 ',' 将忽略换行符
    print(line, end = '')  # 在 Python 3中使用
    line = f.readline()
    line = line[0] + " " + line[2] + " " + line[6]
    print(line)
    line = line[0] + " " + line[4] + " " + line[6]
    print(line)
    line = line[2] + " " + line[4] + " " + line[6]
    print(line)
f.close()


