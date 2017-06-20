# -*- coding:utf-8 -*-

import sys
import os
import pandas as pd
import sqlite3
import numpy as np
import pypinyin



if __name__ == "__main__":
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'yhxx.settings'
    os.system("export DJANGO_SETTINGS_MODULE=yhxx.settings")
    os.environ['DJANGO_SETTINGS_MODULE'] = 'yhxx.settings'
    from django.contrib.auth import authenticate
    from django.contrib.auth.models import User


    xlsfile = './input/2017student.xlsx'
    df = pd.read_excel(xlsfile)
    print df.shape
    print df.columns


    def get_old_edus():
        conn = sqlite3.connect('db.sqlite3')
        old_edus = []
        try:
            cursor = conn.execute('SELECT eduNumber FROM mooc_student')
            for row in cursor:
                if row[0]:
                    old_edus.append(row[0])
        except Exception as e:
            print e
        return old_edus


    old_edus = get_old_edus()
    print "old_edus", old_edus
    narray = np.array(df)
    index_list = ["name", "name_zh", "birthdate", "sex", "eduNumber", "socialNumber", "status", "study_stage", "campus",
                  "grade", "graduationdate", "user_id", "calss_name", "owner"]

    conn = sqlite3.connect('./db.sqlite3')
    for item in narray:
        name = pypinyin.slug(item[0], separator='')
        name_zh = item[0]
        birthdate = item[4]
        sex = item[1]
        eduNumber = item[5]
        socialNumber = None
        status = None
        study_stage = None
        campus = None
        grade = item[2]
        graduationdate = str((6 - int(grade[:1])) + 2016) + "-8-20"
        class_name = item[3]
        owner = item[6]

        def create_new_user(eduNumber, name):
            username = eduNumber
            print 'Creating user {0}.'.format(username)
            user = User.objects.create_user(username=eduNumber, first_name=name)
            password = '123456'
            user.set_password(password)
            user.save()
            assert authenticate(username=eduNumber, password=password)
            print 'User {0} successfully created.'.format(username)

        try:
            rr = User.objects.filter(username=eduNumber)
            #print rr.values()
            if rr:
                user = rr.values()[0]
                userid_id = user["id"]

                print "已经存在此用户，userid_id: ", userid_id
                # if stu["grade"] != grade:
                #     print """this {1} old grade is {1}, but new grade is {2}""".format(userid_id, stu["grade"], grade)
                #
                # if stu["owner"] != owner:
                #     print """this {1} old owner is {1}, but new owner is {2}""".format(userid_id, stu["owner"], owner)
                conn.execute("""UPDATE mooc_student
                                SET grade = '%s', owner='%s'
                                WHERE eduNumber='%s'; """ % (unicode(grade), owner, eduNumber))
                conn.commit()

            else:
                create_new_user(eduNumber, name)
                userid_id = User.objects.filter(username=eduNumber).values()[0]["id"]


            if eduNumber not in old_edus:
                result = (name, name_zh, birthdate, sex, eduNumber, socialNumber, status, study_stage, campus, grade,
                    graduationdate,userid_id, class_name, owner)
                print result
                # 数据插入
                conn.execute("INSERT INTO mooc_student (name, name_zh, birthdate, sex, eduNumber, socialNumber, status, study_stage, campus, grade,graduationdate,userid_id, class_name, owner) \
                      VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                             %(unicode(name), unicode(name_zh), unicode(birthdate), unicode(sex), unicode(eduNumber), unicode(socialNumber), unicode(status), unicode(study_stage), unicode(campus), unicode(grade),
                               unicode(graduationdate), unicode(userid_id), unicode(class_name), unicode(owner)))
                conn.commit()
        except Exception as e:
            print 'There was a problem creating the user: {0}.  Error: {1}.' \
                .format(eduNumber, sys.exc_info()[1])
            print e
            conn.close()




