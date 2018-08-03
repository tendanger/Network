#-*- coding:utf8-*-
#读入数据，交换两列数据，小的在前
import codecs
#/Users/kun/Desktop/
f = codecs.open(r"C://2017//2", "r", "utf-8")
f1 = open(r"C://2017//2_2","a+",encoding='utf-8')

for line in f:
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
f.close()
f1.close()