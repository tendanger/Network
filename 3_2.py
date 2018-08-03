#-*- coding:utf8-*-
#读入数据，将3列关系转为2列关系，并添加权重
import codecs
#/Users/kun/Desktop/
f = codecs.open(r"C://2007//3", "r", "utf-8")
f1 = open(r"C://2007//3_2","a+",encoding='utf-8')

for line in f:
    line.strip().replace('\n', '').replace('\t', '').replace('\r', '').strip()
    line.strip('\n')
    line.strip('\r')
    line_1 =[]
    line_1 = line.split("")

    print(line_1)
    #print(line[0])
    #print(type(line[0]))
    line1 = line_1[0] + " " + line_1[1] #+ " " + str(1)
    f1.write(line1+'\n')
    print(line1)
    line2 = line_1[0] + " " + line_1[2] #+ " " + str(1)
    f1.write(line2+'\n')
    print(line2)
    # line3 = line_1[0] + " " + line_1[3] #+ " " + str(1)
    # f1.write(line3+'\n')
    #print(line3)
    line4 = line_1[1] + " " + line_1[2] #+ " " + str(1)
    f1.write(line4+'\n')
    print(line4)
    # line5 = line_1[1] + " " + line_1[3] + " " + str(1)
    # f1.write(line5+'\n')
    # print(line5)
    # line6 = line_1[2] + " " + line_1[3] + " " + str(1)
    # f1.write(line6+'\n')
    # print(line6)
f.close()
f1.close()
