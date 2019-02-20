#-*- coding: windows-1251 -*-
str1 = "user1;123123;123123123123,434343434"
import datetime
import sys
import sqlite3


param_user = sys.argv[1]# вводим значение юзера и кол-во плат операций в файле
amount = sys.argv[2]


path = "C:/my_custom_path"
connection = sqlite3.connect(path)
#connection.close() - закрывает подкл



curr_date = datetime.datetime.now().strftime("%d.%m.%Y")
curr_time = datetime.datetime.now().strftime("%H:%M:%S")


PREFIX = [  "1CClientBankExchange",
            "ВерсияФормата=1",
            "Кодировка=Windows",
            "Отправитель=Бухгалтерский учет, редакция 4.4",
            "Получатель=ДБО BS-Client v.3 BSS",
            "ДатаСоздания=key:date",
            "ВремяСоздания=key:time",
            "ДатаНачала=key:date",
            "ДатаКонца=key:date",
            "РасчСчет=40702810908000610234"
            ]
#print(len(Prefix))

dictParams = {}#словарь с данными user:[INN,ACC,KPP], user:[INN, ACC, KPP]
user_list = []# список уникальных пользователей
f = open("C:\App\Files\Python\Testing\PayRollsDoc\Info/users.csv","r+")#выгрузка дынных по юзерам
line = f.readline()  # считываем линии
line_count = 0
while line:  # по 1 до конца
    line_count += 1
    data = line.split(';')  # ращделяем строку по ;
    user = data[0]
    if user not in dictParams.keys():#инициализация словаря данных для нового пользователя
        dictParams[user] = {"ACC":data[1]},{"INN":data[2]},{"KPP":data[3].rstrip('\n')}
    else:
        '''
        dictParams[user].append("ACC:",str(data[1]))#!!!! 1:"INN:1",'ACC:2","KPP:3" ?????
        dictParams[user].append("INN:",str(data[2]))
        dictParams[user].append("KPP:",str(data[3].rstrip('\n')))
        '''
    line = f.readline()
f.close()
print(dictParams)



#!!!         TO    DELETE
dictCustom = {}
dictCustom['INN'] = 123
dictCustom['ACC'] = 1234
dictCustom['KPP'] = 12345

#print(dictParams.keys())




DOCUMENT = ["Документ=Платежное поручение",
            "СекцияДокумент=Платежное поручение",
            "Номер=number", #number
            "Дата=28.06.2018",#zamenit
            "Сумма=12.00",
            "ПлательщикСчет=key:ACC",
            "ПлательщикИНН=key:INN", # "ПлательщикИНН=key:INN"
            "ПлательщикКПП=key:KPP",
            "Плательщик1=ООО ИСС",
            "ПлательщикРасчСчет=40702810908000610234", # "ПлательщикРасчСчет=key:RS"
            'ПлательщикБанк1=АКБ "РОСЕВРОБАНК" (АО)',
            'ПлательщикБанк2=Г. МОСКВА',
            'ПлательщикБИК=044525836',
            'ПлательщикКорсчет=30101810445250000836',
            'ПолучательСчет=22222810222222222222',
            'ПолучательИНН=1234567897',
            'ПолучательКПП=131321231',
            'Получатель=ИНН 7777777777 корр бюджетный',
            'Получатель1=корр бюджетный',
            'ПолучательРасчСчет=22222810222222222222',
            'ПолучательБанк1=МИРНИНСКИЙ ФАКБ"АЛМАЗЭРГИЭНБАНК" ОАО',
            'ПолучательБанк2=г. Москва',
            'ПолучательБИК=040001002',
            'ПолучательКорсчет=',
            'ВидПлатежа=Почтой',
            'НазначениеПлатежа=По Основной договор НДС',
            'Очередность=4',
            'ВидОплаты=01',
            'КонецДокумента'
]


file_counter = 0
number = 0

def new_file(user_info, PREFIX, DOCUMENT):# на вход информация о пользователи и 2 шаблона
    #amount = int(input('Amount of Pay Rolls in Doc:'))
    global amount
    global file_counter
    file_counter += 1
    f = open("C:\App\Files\Python\Testing/PayRollsDoc/PayRollsDoc%i.csv" % file_counter, "w+")
    for i in range(0, len(PREFIX)):#проход по строкам Префикса и поиск подстроки key, как заменяемого элемента
        line = PREFIX[i]
        if "key" in line:# при нахождении ключевой строки, в параметризируемые строки записываются текущие дата/время
            line2 = line.split("=")[1]
            line4 = line2.split(':')[1]
            if line4 =='date':
                f.write(line.split("=")[0]+'='+curr_date+'\n')
            elif line4 == 'time':
                f.write(line.split("=")[0]+'='+curr_time+'\n')
        else:
            f.write(PREFIX[i]+'\n')
    for j in range(0, amount):# кол-во платежных поручений задается переменной amount
        global number
        number += 1#увеличение счетчика платежек для юзера
        for k in range(0, len(DOCUMENT)):#проход по строкам Плат.Поручения и поиск подстроки key, как заменяемого элемента
            line = DOCUMENT[k]
            if "number" in line:# замена на номер Плат.Поручения
                line2 = line.split("=")[1]
                f.write(line.split("=")[0]+'='+str(number)+'\n')

            elif "key" in line:#замена key-значений(ИНН и тд)
                #line.split("=")
                line2 = line.split("=")[1]
                #line2.split(":")
                dictkey = line2.split(":")[1]
                if dictkey in dictCustom.keys():
                    f.write(line.split("=")[0]+'='+str(dictParams[user]+'\n'))#!!!!!!ne polniy code

            else:
                f.write(line+'\n')



new_file(3,PREFIX,DOCUMENT)










