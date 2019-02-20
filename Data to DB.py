#-*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("C:\\App\\Soft\\sqlite-tools-win32-x86-3240000\\test1.db")
cursor = connection.cursor()
f = open("C:\\App\\Files\\Python\\XMLcustom\\1С.csv", "r")
line = f.readline()#считываем линии
line_count = 0
while line:#по 1 до конца
    line_count += 1
    line_list = line.split(';')  # ращделяем строку по ;
    ACC = line_list[4].rstrip('\n').lstrip('"').rstrip('"')
    KPP = line_list[3].lstrip('"').rstrip('"')
    INN = line_list[2].lstrip('"').rstrip('"')
    NAME = line_list[1].lstrip('"').rstrip('"')
    print(NAME)
    login = line_list[0]
    number = 1
    task = (ACC, INN, KPP, number, NAME, login)
    sql = '''INSERT INTO corr_users VALUES(?,?,?,?,?,?)'''
    cursor.execute(sql,task)
    line = f.readline()
f.close()
connection.commit()
cursor.close()
connection.close()





