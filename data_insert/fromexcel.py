#! -*- coding:utf-8 -*-
import xlrd
import pandas as pd
import sqlite3
import numpy as np
from pypinyin import pinyin, lazy_pinyin

"""
主要实现的功能是把数据从excel读取出来写入到对应的数据库中,
需要注意的几个问题是,user_id的数据暂时写为null值;
"""

file_name = "/Users/steven/Documents/work-issue/yhxx/1.csv"
data = pd.read_csv(file_name, sep=",", encoding="gb2312")
print data.head()
print len(data)
print data.values[0]
# 经过检查发现暂时在名字这块没有重复的
data_len = len(data)
print len(data[u"姓名"])
print len(np.unique(data[u"姓名"]))
data['name_pinyin'] = [''.join(lazy_pinyin(item)) for item in data[u'姓名']]
data['name_zh'] = data[u"姓名"]

data[u"姓名"]=data[u'教育ID']
data["user_id"] = [i for i in range(11,data_len+11,1)]

print data.head()

print "检查一下,名字的拼音有没有重复的"
print len(np.unique(data["name_pinyin"]))
data.to_csv("/Users/steven/Documents/work-issue/yhxx/1-new.csv",sep=",", header=True, encoding="gb2312",index=False)

# 数据插入
# for i in range(data_len):
#     conn = sqlite3.connect("/Users/steven/PycharmProjects/yhxx/db.sqlite3")
#     item = data.values[i]
#     #data = (i + 3, item[0], item[1], item[6], item[7], item[3], item[2], item[4], item[5])
#     for g in data:
#         print g
#     conn.execute(
#         "INSERT INTO mooc_student (ID,name,sex,birthdate,eduNumber,study_stage, campus, grade, class_name) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
#             i + 3, item[0], item[1], item[6], item[7], item[3], item[2], item[4], item[5]))
#
#     conn.commit()
#
#     print "Records created successfully"
#     conn.close()
