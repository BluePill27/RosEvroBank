#-*- coding: utf-8 -*-


def toFixed(percentage, digits=0):
    return f"{percentage:.{digits}f}"


from datetime import datetime
from time import mktime
f = open("C:\App\Files\Python\Statements\Active 8-15-28-29.csv")
dictUsers = {}#словарь строк
prev_time = 0#инициализация времени 0
users_list = []#список пользователей = dictUsers.keys()
line = f.readline()#считываем линии
line_count = 0
while line:#по 1 до конца
    line_count += 1
    line_list = line.split(';')# разделяем строку по ;
    user = line_list[0]

    str_time = line_list[2].rstrip()  # сохраним дату в формате строки с удалением символа окончания строки справа
    if str_time != "":
        d_time = datetime.strptime(str_time, "%d.%m.%Y")  # конвертируем строку в дату
        s_time = mktime(d_time.timetuple())  # конвертируем из даты в секунды
        date_from = s_time / 86400

    str_time = line_list[3].rstrip()  # сохраним дату в формате строки с удалением символа окончания строки справа
    if str_time != "":
        d_time = datetime.strptime(str_time, "%d.%m.%Y")  # конвертируем строку в дату
        s_time = mktime(d_time.timetuple())  # конвертируем из даты в секунды
        date_to = s_time / 86400#переводим секунды в дни

    period = date_to - date_from + 1# чтобы выписка бралась за 1 день, а не за 0 (27.12-27.12 :1 день)

    if user not in users_list:#если юзер встречается в первый раз
        users_list.append(user)#добавляем юзера в список юзеров # delete
        dictUsers[user] = [period,]#инициализируем список для последнего ключа списком с текущей операцией

    dictUsers[user].append(period)

    line = f.readline()

f.close()  # выходим из файлa


'''
Создаем словарь период выписки: % от всех пользователей сделавших такую выписку
'''

dictPeriods = {}# period:user1, user2, user3
user_count = 0

for user in dictUsers:
    for period in dictUsers[user]:
        if period not in dictPeriods:
            dictPeriods[period] = []

for user in dictUsers:
    for period in dictUsers[user]:
        user_count = 0
        if user not in dictPeriods[period]:
            dictPeriods[period].append(user)
            user_count +=1

sum = 0# процент обработанных выписок

#Не сгруппиров по 5% признаку

for period in dictPeriods:
    percentage = ((len(dictPeriods[period]))/(len(users_list))*100)
    sum+=percentage
    print(toFixed(period, 0), len(dictPeriods[period]), toFixed(percentage, 3),"%")


'''
#Сгруппировать по 5% признаку

low_periods = []
low_counter = 0
for period in dictPeriods:#вывод кол-ва пользователей для кол-в поручений в файлах
    percentage = ((len(dictPeriods[period]))/(len(users_list))*100)
    sum +=percentage
    if percentage >=5:#кол-во операций чье процентное соотношение >5% публикуются отдельно
        print(toFixed(period, 0), len(dictPeriods[period]), toFixed(((len(dictPeriods[period]))/(len(users_list))*100), 3),"%")
        prev_percentage = 0
    else:
        if percentage <=5:# если % операций <5, то они складываются в список до момента достижения 5% вместе
            low_periods.append(period)# к списку операций входящих в стак (меньше 5%) прибавляется текущая рассматриваемая
            low_counter += len(dictPeriods[period])#к сумме операций стака прибавляем сумму текущих операций
            prev_percentage += percentage# процент стака от общего
            if prev_percentage >= 5:# когда суммарный % операций => 5%
                print(low_periods[0],"-", low_periods[len(low_periods)-1], low_counter, toFixed(prev_percentage,3), "%")#вывод диапазона операций вошедших в стак, чей суммарный % перевалил за 5%
                prev_percentage = 0#сброс счетчиков процентов, списка операций и суммы операций
                low_periods.clear()
                low_counter = 0
            elif period == max:# если % стака операций не набрал 5%, а файл закончился
                print(low_periods[0], "-", low_periods[len(low_periods) - 1], low_counter, toFixed(prev_percentage,3),"%")  # вывод диапазона операций вошедших в стак, чей суммарный % перевалил за 5%
'''

print(sum, "%")
print(len(users_list))