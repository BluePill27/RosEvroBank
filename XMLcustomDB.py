import datetime
import sys
import sqlite3

param_user = int(sys.argv[1])# вводим значение юзера и кол-во плат операций в файле
param_amount = int(sys.argv[2])
#param_user = 1
#param_amount = 3

curr_date = datetime.datetime.now().strftime("%d.%m.%Y")
curr_time = datetime.datetime.now().strftime("%H:%M:%S")

#file_counter = 0
dictUsers = {}

PREFIX = [  "1CClientBankExchange",
            "ВерсияФормата=1",
            "Кодировка=Windows",
            "Отправитель=Бухгалтерский учет, редакция 4.4",
            "Получатель=ДБО BS-Client v.3 BSS",
            "ДатаСоздания=key:date",#!!
            "ВремяСоздания=key:time",#!!
            "ДатаНачала=key:date",
            "ДатаКонца=key:date",
            "РасчСчет=key:ACC"#!!
            ]

DOCUMENT = ["Документ=Платежное поручение",
            "СекцияДокумент=Платежное поручение",
            "Номер=key:number", #number
            "Дата=key:date",#zamenit
            "Сумма=12.00",
            "ПлательщикСчет=key:ACC",
            "ПлательщикИНН=key:INN", # "ПлательщикИНН=key:INN"
            "ПлательщикКПП=key:KPP",
            "Плательщик1=ООО ИСС",
            "ПлательщикРасчСчет=key:ACC", # "ПлательщикРасчСчет=key:RS"
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

EOF = ["КонецФайла"]

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error:
        print(Error)
    return None

def select_user_to_dictionary(connection,task):
    sql = ''' SELECT * FROM USERS 
              WHERE id = ? '''
    current = connection.cursor()
    current.execute(sql,task)
    row = current.fetchall()
    #print(row)
    dictUsers = {'ID':row[0][0],"ACC": int(row[0][1]), "INN": int(row[0][2]), "KPP": int(row[0][3]),'number':int(row[0][4])}# row[0]
    #print(dictUsers)
    dictUsers['number'] += param_amount
    #print(dictUsers)
    return dictUsers

def update_number(connection, task):
    sql = ''' UPDATE Users
              SET number = ?
              WHERE id = ?  '''
    current = connection.cursor()
    current.execute(sql,task)

def update_number(connection, task):
    sql = ''' UPDATE Users
              SET number = ?
              WHERE id = ?  '''
    current = connection.cursor()
    current.execute(sql,task)

def main ():
    database = "C:\App\Soft\sqlite-tools-win32-x86-3240000/test1.db"
    connection = create_connection(database)
    with connection:
        dictUsers = (select_user_to_dictionary(connection, (param_user,)))#передаем подключение и параметр ИД для выборки из базы
        update_number(connection, (dictUsers['number'], param_user))
    return dictUsers
    connection.close()






def new_file(PREFIX, DOCUMENT,EOF):# на вход информация о пользователи и 2 шаблона
    global file_counter#документ хранящий переменную с чтением из него и записью?
    file_counter = 1#новый документ с индексом file_counter
    f = open("C:\App\Files/Python/Testing/PayRollsDoc/user-%i_Platejek-%i.csv" % ((dictUsers['ID']), (param_amount)), "w+")
    #Files/Python/Testing/PayRollsDoc/
    for i in range(0, len(PREFIX)):#проход по строкам Префикса и поиск подстроки key, как заменяемого элемента
        line = PREFIX[i]
        if "key" in line:# при нахождении ключевой строки, в параметризируемые строки записываются текущие дата/время
            line2 = line.split("=")[1]
            line4 = line2.split(':')[1]
            if line4 =='date':
                f.write(line.split("=")[0]+'='+curr_date+'\n')
            elif line4 == 'time':
                f.write(line.split("=")[0]+'='+curr_time+'\n')
            elif line4 =='ACC':
                f.write(line.split("=")[0]+'='+str(dictUsers['ACC'])+'\n')
        else:
            f.write(PREFIX[i]+'\n')
    curr_counter = dictUsers['number'] - param_amount
    for j in range(0, param_amount):# кол-во платежных поручений задается переменной amount
        #print(curr_counter)
        for k in range(0, len(DOCUMENT)):#проход по строкам Плат.Поручения и поиск подстроки key, как заменяемого элемента
            line = DOCUMENT[k]
            if "key" in line:  # при нахождении ключевой строки, в параметризируемые строки записываются текущие дата/время
                line2 = line.split("=")[1]
                line4 = line2.split(':')[1]
                if line4 =='number':
                    f.write(line.split("=")[0] + '=' + str(curr_counter) + '\n')
                elif line4 == 'ACC':
                    f.write(line.split("=")[0] + '=' + str(dictUsers['ACC']) + '\n')
                elif line4 == 'INN':
                    f.write(line.split("=")[0] + '=' + str(dictUsers['INN']) + '\n')
                elif line4 == 'KPP':
                    f.write(line.split("=")[0] + '=' + str(dictUsers['KPP']) + '\n')
                elif line4 =='date':
                    f.write(line.split("=")[0] + '=' + curr_date + '\n')
            else:
                f.write(line+'\n')
        curr_counter+=1
    file_counter +=1
    for h in range (0,len(EOF)):
        line = EOF[h]
        f.write(line + '\n')


if __name__ =='__main__':
    dictUsers = main()
    new_file(PREFIX,DOCUMENT,EOF)

print("Current_User",dictUsers)

