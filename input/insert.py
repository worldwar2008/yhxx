# -*- coding:utf-8 -*-

import xlrd
import pandas as pd
import sqlite3
import numpy as np
from datetime import datetime
import pypinyin

xlsfile = './2017student.xlsx'
df = pd.read_excel(xlsfile)
print df.shape
print df.columns


def get_old_edus():
    conn = sqlite3.connect('../db.sqlite3')
    old_edus = []
    try:
        cursor = conn.execute('select eduNumber from mooc_student')
        for row in cursor:
            if row[0]:
                old_edus.append(row[0])
    except Exception as e:
        print e
    return old_edus

old_edus = get_old_edus()
narray = np.array(df)
index_list=["name","name_zh","birthdate","sex","eduNumber","socialNumber","status","study_stage","campus","grade","graduationdate","user_id","calss_name","owner"]

#conn = sqlite3.connect('../db.sqlite3')
for item in narray[:100]:
    name=pypinyin.slug(item[0],separator='')
    name_zh=item[0]
    birthdate=item[4]
    sex=item[1]
    eduNumber=item[5]
    socialNumber=None
    status=None
    study_stage=None
    campus=None
    grade=item[2]
    graduationdate=str((6-int(grade[:1]))+2016)+"-8-20"
    class_name=item[3]
    owner=item[6]
    
    try:
        print 'Creating user {0}.'.format(eduNumber)
        user = User.objects.create_user(username=eduNumber, first_name=name)
        user.set_password('123456')
        user.save()
        assert authenticate(username=username, password=password)
        print 'User {0} successfully created.'.format(username)

    except:
        print 'There was a problem creating the user: {0}.  Error: {1}.' \
            .format(username, sys.exc_info()[1])

    userid_id = user.id
    if eduNumber not in old_edus:
        result = (name,name_zh,birthdate,sex,eduNumber,socialNumber,status,study_stage,campus,grade,graduationdate,user_id,class_name,owner)
        for i in result:
            print i




































