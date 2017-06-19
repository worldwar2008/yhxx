# -*- coding:utf-8 -*-
from datetime import datetime

month_milestone = 6

def get_course_year():
    now_date = datetime.now().date()
    if (now_date.month < month_milestone):
        # 9月份之前显示上学期的课程,9月份之后显示下学期的选择的课程
        course_year = str(now_date.year-1)+"-"+str(now_date.year)
        #print "course_year",course_year
        return course_year
    else:
        #9月份之后,列表就会显示下学年的课程了
        course_year = str(now_date.year)+"-"+str(now_date.year+1)
        #print "course_year", course_year
        return course_year
