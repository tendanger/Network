#-*- coding:utf8-*-
#读入数据，交换两列数据，小的在前
import codecs
import time
#/Users/kun/Desktop/
f0 = codecs.open(r"C://2017//2", "r", "utf-8")
f1 = open(r"C://2017//2_2","a+",encoding='utf-8')

for line in f0:
    line.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
    line.strip('\n')
    line.strip('\r')
    print(line)
    #line.replace("\r", "")
    #line.replace("\n", "")
    line_1 =[]
    line_1 = line.split()


    print(line_1[0])
    print(line_1[1])
    print(line_1)

    #print(line[0])
    #print(type(line[0]))
    if line_1[0] > line_1[1]:
        line1 = line_1[1] + " " + line_1[0] #+ " " + str(1)
        print(line1)
        f1.write(line1+'\n')
        #f1.write(line1)
    elif line_1[0] < line_1[1]:
        line1 = line_1[0] + " " + line_1[1] #+ " " + str(1)
        f1.write(line1+'\n')
        #f1.write(line1)
        #print(line1)
    # print(line2)
    # line3 = line_1[0] + " " + line_1[3] #+ " " + str(1)
    # f1.write(line3+'\n')
    #print(line3)
    # line4 = line_1[1] + " " + line_1[2] #+ " " + str(1)
    # f1.write(line4+'\n')
    # print(line4)
    # line5 = line_1[1] + " " + line_1[3] + " " + str(1)
    # f1.write(line5+'\n')
    # print(line5)
    # line6 = line_1[2] + " " + line_1[3] + " " + str(1)
    # f1.write(line6+'\n')
    # print(line6)
f0.close()
f1.close()


time.sleep(3)
#-*- coding:utf8-*-
#读入文本，判断重复的次数
import codecs
#/Users/kun/Desktop/
f2 = codecs.open(r"C://2017//2_2", "r", "utf-8")
f3 = open(r"C://2017//2017_f","a+",encoding='utf-8')
# text = f.read()
# length = len(text.splitlines())
arr = []
line1 = ""
for line in f2:
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
    f3.write(str(item)+" "+str(temp3.count(item))+'\n')
f2.close()
f3.close()

time.sleep(3)
#-*- coding:utf8-*-
#讲文本转化为.net文件
#import networkx as nx
import networkx as nx
### read edge list to networkx ###/Users/kun/Desktop/
# the format of each line: (src dst whole_duration/total_duration total_duration)
G = nx.Graph()
for line in open("C://2017/2017_f", encoding='UTF-8'):
#for line in open("/Users/kun/Desktop/", encoding='UTF-8'):
#for line in open("/Users/kun/Desktop/2017/2017_f", encoding='UTF-8'):
    strlist = line.split(" ")
    print(strlist)
    n1 = str(strlist[0])
    n2 = str(strlist[1])
    weight = float(strlist[2])
    G.add_weighted_edges_from([(n1, n2, weight)]) #G.add_edges_from([(n1, n2)])

import matplotlib.pyplot as plt
#assign node ID as nodes' label. G.nodes return a list of nodes, convert list to dict

nx.draw(G)
nx.write_pajek(G, "C://2017//2017_f.net", encoding='UTF-8')
nx.write_gexf(G, "C://2017//2017_f.gexf", encoding='UTF-8')
#labels = dict((i,i) for i in G.nodes())

#print(labels)
#nx.draw_networkx_labels(G, pos=nx.spring_layout(G), labels = labels)
#plt.savefig(filename)

#plt.show()

