#-*- coding: utf-8 -*-

from datetime import datetime
from time import mktime

def toFixed(percentage, digits=0):
    return f"{percentage:.{digits}f}"

f = open("C:\App\Files\Python\Statements\Special29.12 By ID.csv")
dictPeriods = {}#словарь строк
start_time = 0 #инициализация времени 0
periods_list = []#список пользователей = dictUsers.keys()
date_from_list = []#с какого числа запрос
date_to_list = []#по какое число запрос
line = f.readline()#считываем линии
line_count = 0
while line:#по 1 до конца
    line_count += 1
    line_list = line.split(';')  # разделяем строку по ;

    str_time_from = line_list[2].rstrip()  # сохраним дату в формате строки с удалением символа окончания строки справа
    str_time_to = line_list[3].rstrip()  # сохраним дату в формате строки с удалением символа окончания строки справа
    if str_time_from !="" and str_time_to != "":
        d_time = datetime.strptime(str_time_from, "%d.%m.%Y")  # конвертируем строку в дату
        #print (d_time, line_list[4])
        s_time = mktime(d_time.timetuple())  # конвертируем из даты в секунды
        date_from = s_time/86400
        date_from_list.append(date_from)

        d_time = datetime.strptime(str_time_to, "%d.%m.%Y")  # конвертируем строку в дату
        s_time = mktime(d_time.timetuple())  # конвертируем из даты в секунды
        date_to = s_time/86400
        date_to_list.append(date_to)
    else:
        print("Bad string: " + line)


    period = date_to-date_from+1#чтобы выписка бралась за 1 день, а не за 0
    if period not in periods_list:
        periods_list.append((period))
        dictPeriods[(period)] = 0#инициализация значения 0

    line = f.readline()

f.close()#выходим из файла



#print(periods_list)
#print((dictPeriods))

max = 0
for period in dictPeriods:#находим максимальную разность дат в выписке
    if period > max:
        max = period

#print(max)
#print(periods_list.sort())
for i in range (0, len(date_from_list)):
    #print(i)
    if (date_from_list[i] > date_to_list[i]):
        print("incorrect dates at line :" + str(i) + " DATE_TO: " + str(date_to_list[i]) + " < DATE_FROM: " + str(date_from_list[i]))
    else:
        period = date_to_list[i] - date_from_list[i] + 1  # чтобы выписка бралась за 1 день, а не за 0
        if period > 0:
            dictPeriods[period] =  dictPeriods[period] + 1#учеличиваем счетчик таких выписок на 1

sum = 0
print("Кол-во дней/","Кол-во выписок/","Процент от общего кол-ва")

'''
#Не сгрупированный вывод

for period in dictPeriods:
    percentage = ((dictPeriods[period]/line_count)*100)
    sum+=percentage
    print(period, dictPeriods[period], toFixed(percentage,3),"%", "\n")
print("Обработанный процент операций:",sum, "%")
print(dictPeriods)
'''





#Сгруппированный вывод

low_periods = []
low_counter = 0

for period in dictPeriods:
    percentage = ((dictPeriods[period] / line_count) * 100)#процентное соотношение записей от основного
    sum +=percentage#проверка на то, что учтены все операции
    if percentage >=5:#кол-во операций чье процентное соотношение >5% публикуются отдельно

        print(period, dictPeriods[period], toFixed(percentage, 3), "%", "\n")
        prev_percentage = 0
    else:
        if percentage <=5:# если % операций <5, то они складываются в список до момента достижения 5% вместе
                low_periods.append(period)# к списку операций входящих в стак (меньше 5%) прибавляется текущая рассматриваемая
                low_counter += dictPeriods[period]#к сумме операций стака прибавляем сумму текущих операций
                prev_percentage += percentage# процент стака от общего
                if prev_percentage >= 5:# когда суммарный % операций => 5%
                    print(low_periods[0],"-",low_periods[len(low_periods)-1], low_counter, prev_percentage,'%','\n' )#вывод диапазона операций вошедших в стак, чей суммарный % перевалил за 5%
                    prev_percentage = 0#сброс счетчиков процентов, списка операций и суммы операций
                    low_periods.clear()
                    low_counter = 0
                elif period == max:# если % стака операций не набрал 5%, а файл закончился
                    print(low_periods[0], "-", low_periods[len(low_periods) - 1], low_counter, prev_percentage,'%','\n')

print(sum)
print(dictPeriods)
total = 0
for period in dictPeriods:
    total+=period*dictPeriods[period]
print(total)