# -*- coding: utf-8 -*-
#526电脑，10线程
#20180405
#patent_hit
from lxml import etree
#from scrapy.selector import Selector
import codecs
import pymysql
import threading
import time
####################
#处理大学的简写
patent_u = "hit"
#线程1处理页面范围
t1_start =1
t1_stop =300
#线程2处理页面范围
t2_start =301
t2_stop =600
#线程3处理页面范围
t3_start =601
t3_stop =900
#线程4处理页面范围
t4_start =901
t4_stop =1200
###################
t5_start =1201
t5_stop =1500
###################
t6_start =1501
t6_stop =1800
###################
t7_start =1801
t7_stop =2100
###################
t8_start =2101
t8_stop =2400
###################
t9_start =2401
t9_stop =2700
###################
t10_start =2700
t10_stop =3000
###################



#定义函数
def dealData1( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page_start = page_start
    page_stop = page_stop
    #输入大学名称简写
    patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
#进程2
def dealData2( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
#进程3
def dealData3( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
#进程4
def dealData4( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData5( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData6( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData7( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData8( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData9( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
def dealData10( page_start,page_stop, patent):
    ##########################
    #输入专利页面数量
    page = page_start
    page = page_stop
    #输入大学名称简写
    #patent = patent
    ##########################
    #print(page)
    #print(patent)


    #数据库连接信息
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='Kun123_567',
        db='patent_info',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor()
    #print(conn)
    #print(cursor)

    #读取文件
    #html_1 = codecs.open("/Users/kun/Desktop/Patent/patent10.html", "r", "utf-8")
    #处理1-10页数据
    print("*********")
    print("开始处理数据")

    try:
        for j in range(page_start, page_stop+1):
            print("**********************")
            print("**********************")
            print("正在处理第%d页数据"%j)
            html = codecs.open(r"D://patent_"+ patent +"//patent" + str(j) + ".html", "r", "utf-8")

            content = html.read()
            html.close()
            #页面解析
            page_source = etree.HTML(content)
            for i in range(1,13):
                print("--第" + str(j) + "页，第" + str(i) + "条专利--")
                #print("专利条数"+str(i))
                #第一条专利信息
                #xpatn语句
                title_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/h1/div[2]/a/b/text()")
                ipc_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[5]/span/a/text()")
                id_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[1]/text()")
                # holder_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span/a/font/text()")

                holder_1_0 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/font/text()")
                holder_1_1 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[1]/a/text()")
                holder_1_2 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/font/text()")
                holder_1_3 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[2]/a/text()")
                holder_1_4 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/font/text()")
                holder_1_5 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[3]/a/text()")
                holder_1_6 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/font/text()")
                holder_1_7 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[4]/a/text()")
                holder_1_8 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/font/text()")
                holder_1_9 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[5]/a/text()")
                holder_1_10 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/font/text()")
                holder_1_11 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[6]/a/text()")
                holder_1_12 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/font/text()")
                holder_1_13 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[7]/a/text()")
                holder_1_14 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/font/text()")
                holder_1_15 = page_source.xpath(
                    "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[6]/span[8]/a/text()")
                #print(holder_1_3)
                #创建列表
                #for i in range(1, 9):
                #    print("列表条数" + str(i))
                 #   locals()['lst' + str(i)] = []
                #合并1和2,3和4的联合申请人
                lst1 = []
                lst2 = []
                lst3 = []
                lst4 = []
                lst5 = []
                lst6 = []
                lst7 = []
                lst8 = []
                lst1.append(''.join(map(str, holder_1_0 + holder_1_1)))
                lst2.append(''.join(map(str, holder_1_2 + holder_1_3)))
                lst3.append(''.join(map(str, holder_1_4 + holder_1_5)))
                lst4.append(''.join(map(str, holder_1_6 + holder_1_7)))
                lst5.append(''.join(map(str, holder_1_8 + holder_1_8)))
                lst6.append(''.join(map(str, holder_1_10 + holder_1_11)))
                lst7.append(''.join(map(str, holder_1_12 + holder_1_13)))
                lst8.append(''.join(map(str, holder_1_14 + holder_1_15)))
                holder_1 = lst1 + lst2 + lst3 + lst4 + lst5 + lst6 + lst7 + lst8
                #print(holder_1)
                date_1 = page_source.xpath(
                        "//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[2]/div/p[2]/a/text()")
                group_1 = page_source.xpath("//*[@id='search_result_former']/div[4]/div[1]/ul/li["+str(i)+"]/div/div[1]/div/a[2]/text()")
                # print(holder_1)
                # 处理专利名称信息
                for i in range(len(title_1)):
                #    print("title条数" + str(i))
                    # title_1[i] = title_1[i].replace(' ', '')
                    title_1[i] = title_1[i].replace("'", "")
                    title_1[i] = title_1[i].replace(")", "")
                    title_1[i] = title_1[i].replace('(', '')
                #    print(title_1)
                # 处理同族信息
                for i in range(len(group_1)):
                #    print("group条数" + str(i))
                    group_1[i] = group_1[i].replace(' ', '')
                    group_1[i] = group_1[i].replace('\r', '')
                    group_1[i] = group_1[i].replace('\n', '')
                    group_1[i] = group_1[i].replace('\t', '')
                for i in range(len(group_1)):
                #    print("len(group)条数" + str(i))
                    group_1[i] = group_1[i].replace('同族：', '')
                # 处理专权人信息
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    # holder_1[0] = '东北大学'
                    holder_1[i] = holder_1[i].replace(' ', '')
                    holder_1[i] = holder_1[i].replace('\r', '')
                    holder_1[i] = holder_1[i].replace('\n', '')
                    holder_1[i] = holder_1[i].replace('\t', '')
                #print(holder_1)
                # print(holder_1)
                for i in range(len(holder_1)):
                #    print("len(holder)条数" + str(i))
                    if '' in holder_1:
                        holder_1.remove('')

                #print(holder_1)
                # 处理ipc_1分类号信息
                for i in range(len(ipc_1)):
                #    print("len(ipc)条数" + str(i))
                    ipc_1[i] = ipc_1[i].replace(' ', '')
                    ipc_1[i] = ipc_1[i].replace('\r', '')
                    ipc_1[i] = ipc_1[i].replace('\n', '')
                    ipc_1[i] = ipc_1[i].replace('\t', '')
                # 打印信息
                # print(id_1)
                # print(date_1)
                # print(title_1)
                # print(ipc_1)
                # print(holder_1)
                # print(group_1)

                # 合并ipc_1信息
                ipc_1_joint = ','.join(map(str, ipc_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                ipc_1_one = list()
                ipc_1_one.append(ipc_1_joint)
                # 合并专权人信息
                holder_1_joint = ','.join(map(str, holder_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                holder_1_one = list()
                holder_1_one.append(holder_1_joint)
                #print(holder_1_one)
                # 合并title信息
                title_1_joint = ''.join(map(str, title_1))  # join 操作不是 str类型的列表会报错，得先转换哈
                # ipc_1_joint = eval(str(ipc_1).replace(',','').replace(' ',''))
                title_1_one = list()
                title_1_one.append(title_1_joint)
                # 打印合并信息
                # print("*" * 10)
                # print("*" * 180)
                # print("   第" + str(j) + "页   " )
                # print("*" * 10)
                c_1 = id_1 + date_1 + title_1_one + holder_1_one + ipc_1_one + group_1
                sql_insert = "INSERT INTO "+patent+"(p_id,p_date,p_title,p_holder,p_ipc,p_group) VALUES ( '" + str(
                    c_1[0]) + "','" + str(c_1[1]) + "','" + str(c_1[2]) + "','" + str(c_1[3]) + "','" + str(
                    c_1[4]) + "','" + str(c_1[5]) + "');"
                # 执行语句
                # cursor.execute(sql, ( "'"+str(timelist_id[i])+"','"+str(timelist_time[i])+"','"+str(timelist_name[i])+"','"+str(timelist_holder[i])+"','"+str(timelist_addre[i])+"'"))
                cursor.execute(sql_insert)
                # sql = "truncate table hit;"
                # cursor.execute(sql)
                # 事务提交，否则数据库得不到更新
                #conn.commit()
                #print("success")
                # print(cursor.rowcount)
                #print(c_1)
                #print(i)

    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()
        cursor.close()
        print('*********************')
        print('程序执行完毕！')
#定义线程
try:
   t1 = threading.Thread(target = dealData1, args = (t1_start,t1_stop, patent_u,))
   t1.start()
   t2 = threading.Thread(target = dealData2, args = (t2_start,t2_stop, patent_u,))
   t2.start()
   t3 = threading.Thread(target = dealData3, args = (t3_start,t3_stop, patent_u,))
   t3.start()
   t4 = threading.Thread(target = dealData4, args = (t4_start,t4_stop, patent_u,))
   t4.start()
   t5 = threading.Thread(target=dealData5, args=(t5_start, t5_stop, patent_u,))
   t5.start()
   t6 = threading.Thread(target=dealData6, args=(t6_start, t6_stop, patent_u,))
   t6.start()
   t7 = threading.Thread(target=dealData7, args=(t7_start, t7_stop, patent_u,))
   t7.start()
   t8 = threading.Thread(target=dealData8, args=(t8_start, t8_stop, patent_u,))
   t8.start()
   t9 = threading.Thread(target=dealData9, args=(t9_start, t9_stop, patent_u,))
   t9.start()
   t10 = threading.Thread(target=dealData10, args=(t10_start, t10_stop, patent_u,))
   t10.start()
   #threading.Thread(target = dealData, args = (10, "neu_temp",))
except:
   print("Error: unable to start thread")

