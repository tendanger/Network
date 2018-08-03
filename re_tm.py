#-*- coding:utf8-*-
#读入文本，判断重复的次数
import codecs
#/Users/kun/Desktop/
f = codecs.open(r"C://2017//2_2", "r", "utf-8")
f1 = open(r"C://2017//2017_f","a+",encoding='utf-8')
# text = f.read()
# length = len(text.splitlines())
arr = []
line1 = ""
for line in f:
    #print(line)
    # mylist = []
    #将每一行数据，去掉行尾的换行符后，以逗号相连，组成新的字符串
    line1 = line1 + line.rstrip() + ","
    # 去掉每行最后的换行符'\n'
    temp1 = line1.strip('\n')
    temp2 = temp1.strip('\r')
    #print(temp2)
    #把temp2字符串，以逗号分隔，组成列表
    temp3 = temp2.split(',')
    #删除列表中的空元素
    while '' in temp3:
        temp3.remove('')
#set取出唯一元素，只能处理列表，所以需要处理为temp3列表
myset = set(temp3)
    # print(myset)
    #
for item in myset:
    print(item, temp3.count(item))
    f1.write(str(item)+" "+str(temp3.count(item))+'\n')
f1.close()


# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
# print(arr[5])
# print(len(arr))
# a = {}
# for i in arr:
#     #print(i)
#     if arr.count(i) >= 1:
#     #print(arr.count(i))
#         a[i] = arr.count(i)
#
#     print(a)



f.close()