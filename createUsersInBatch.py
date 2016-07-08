# #! -*- coding:utf-8 -*-
# import sys
# import os
# import numpy as np
# import pandas as pd
# from django.contrib.auth import authenticate
#
#
# if __name__ == '__main__':
#
#     # os.environ['DJANGO_SETTINGS_MODULE'] = 'yhxx.settings'
#     os.system("export DJANGO_SETTINGS_MODULE=yhxx.settings")
#
#     from django.contrib.auth.models import User
#
#     #  Update the users in this list.
#     #  Each tuple represents the username, password, and email of a user.
#     users = [
#         ('user_1', 'phgzHpXcnJ', 'user_1@example.com'),
#         ('user_2', 'ktMmqKcpJw', 'user_2@example.com'),
#     ]
#     file_name = "/Users/steven/Documents/work-issue/yhxx/1-new.csv"
#     data = pd.read_csv(file_name, sep=",", encoding="gb2312")
#     print users
#     print data.head()
#     new_data = data.loc[:, [u"姓名","name_pinyin","name_pinyin"]]
#     print new_data.head()
#     new_users = []
#     for item in np.array(new_data):
#         new_users.append((item[0],item[1],item[2]))
#     print new_users
#
#
#     for username, password, first_name in new_users:
#         try:
#             print 'Creating user {0}.'.format(username)
#             user = User.objects.create_user(username=username, first_name=first_name)
#             user.set_password(password)
#             user.save()
#
#             assert authenticate(username=username, password=password)
#             print 'User {0} successfully created.'.format(username)
#
#         except:
#             print 'There was a problem creating the user: {0}.  Error: {1}.' \
#                 .format(username, sys.exc_info()[1])