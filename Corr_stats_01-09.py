#-*- coding: utf-8 -*-

#Список операций вошедших в профиль нагрузки
ListOper = ['Платежное поручение', 'Запрос на получение информации о движении средств', 'Письмо в банк']
#Запись в файл с результатами !Задать корректный путь!
with open("C:\\Users\\Chankin432\\Desktop\\01-09_result.csv", "w") as file:
    for i in range(1, 10):
        #Считывание информации файл за файлом из выборки месяцев !Задать корректный путь! !Унифицировать имена файлов!
        f = open("C:\\Users\\Chankin432\\Desktop\\0%s18_crqts.csv" % i, "r")
        line = f.readline()
        dictOper = {}
        while line:
            line_list = line.split(';')
            type = line_list[0]
            amount = int(line_list[1])
            date = line_list[2]
            hour = int(line_list[3].rstrip('\n'))

            #проверяем если в словаре 1 уровня текущая дата
            #проверяем если в словаре 2 уровня текущее время
            #проверяем есть ли в словаре 3 уровня текущий тип операции и соответствует ли он операциям из профиля
            #записываем словарь слов[дата] = {[операция]:кол-во, [операция]:кол-во, ...}

            if date not in dictOper.keys():
                dictOper[date] = {}
                if hour not in dictOper[date].keys():
                    dictOper[date][hour] = {}
                    if type not in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] = amount
                    elif type in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] += amount
                else:
                    if type not in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] = amount
                    elif type in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] += amount

            else:
                if hour not in dictOper[date].keys():
                    dictOper[date][hour] = {}
                    if type not in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] = amount
                    elif type in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] += amount
                else:
                    if type not in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] = amount
                    elif type in dictOper[date][hour].keys() and type in ListOper:
                        dictOper[date][hour][type] += amount
            line = f.readline()
        f.close()

        #Инициалзация переменных отвечающих  за раниение макс кол-ва операций, даты, часа
        #Группировка данных для одного промежутка времени
        #Поиск промежутка с наибольшим кол-вом операций в нем
        max = 0
        max_date = ''
        max_hour = 0
        for date in dictOper.keys():
            for hour in dictOper[date].keys():
                curr = 0
                for type in dictOper[date][hour].keys():
                    curr += dictOper[date][hour][type]
                if curr > max:
                    max = curr
                    max_date = date
                    max_hour = hour
        print(max)
        print(max_date, max_hour)
        print(dictOper[max_date][max_hour])

        #Запись м результирующий файл
        file.write('month: ' + max_date.split('.')[0] + '; '
                   + 'date: ' + max_date.split('.')[1] + '; '
                   + 'hour: ' + str(max_hour) + '; '
                   + 'operations: ' + str(max) + '\n')
        for type in ListOper:
            if type in dictOper[max_date][max_hour].keys():
                file.write(type + ': ' + str(dictOper[max_date][max_hour][type])+'\n')
        file.write('\n')

