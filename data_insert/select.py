# #!/usr/bin/python
#
# import sqlite3
#
# conn = sqlite3.connect('db.sqlite3')
# print "Opened database successfully";
#
# cursor = conn.execute("SELECT username, date_joined from auth_user")
# for row in cursor:
#    print "username = ", row[0]
#    print "date_joined = ", row[1], "\n"
#
# print "Operation done successfully";
# conn.close()