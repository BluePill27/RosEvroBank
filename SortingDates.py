#-*- coding: utf-8 -*-
f = open("C:\App\Files\Python\PaysInFile/2017.12 By Id.csv", "r")
file = open("C:\App\Files\Python\PaysInFile\8-15-28-29.csv", "w")
line = f.readline()#считываем линии
line_count = 0
while line:#по 1 до конца
    line_count += 1
    line_list = line.split(';')  # ращделяем строку по ;
    user = line_list[0]
    date = line_list[1]
    time = line_list[2].rstrip('\n')
    file.write(user+";"+date+";"+time+'\n')
    line = f.readline()
f.close()
file.close()




