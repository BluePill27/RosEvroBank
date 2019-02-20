#-*- coding: windows-1251 -*-
str1 = "user1;123123;123123123123,434343434"
import datetime
import sys
import sqlite3


param_user = sys.argv[1]# ������ �������� ����� � ���-�� ���� �������� � �����
amount = sys.argv[2]


path = "C:/my_custom_path"
connection = sqlite3.connect(path)
#connection.close() - ��������� �����



curr_date = datetime.datetime.now().strftime("%d.%m.%Y")
curr_time = datetime.datetime.now().strftime("%H:%M:%S")


PREFIX = [  "1CClientBankExchange",
            "�������������=1",
            "���������=Windows",
            "�����������=������������� ����, �������� 4.4",
            "����������=��� BS-Client v.3 BSS",
            "������������=key:date",
            "�������������=key:time",
            "����������=key:date",
            "���������=key:date",
            "��������=40702810908000610234"
            ]
#print(len(Prefix))

dictParams = {}#������� � ������� user:[INN,ACC,KPP], user:[INN, ACC, KPP]
user_list = []# ������ ���������� �������������
f = open("C:\App\Files\Python\Testing\PayRollsDoc\Info/users.csv","r+")#�������� ������ �� ������
line = f.readline()  # ��������� �����
line_count = 0
while line:  # �� 1 �� �����
    line_count += 1
    data = line.split(';')  # ��������� ������ �� ;
    user = data[0]
    if user not in dictParams.keys():#������������� ������� ������ ��� ������ ������������
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




DOCUMENT = ["��������=��������� ���������",
            "��������������=��������� ���������",
            "�����=number", #number
            "����=28.06.2018",#zamenit
            "�����=12.00",
            "��������������=key:ACC",
            "�������������=key:INN", # "�������������=key:INN"
            "�������������=key:KPP",
            "����������1=��� ���",
            "������������������=40702810908000610234", # "������������������=key:RS"
            '��������������1=��� "�����������" (��)',
            '��������������2=�. ������',
            '�������������=044525836',
            '�����������������=30101810445250000836',
            '��������������=22222810222222222222',
            '�������������=1234567897',
            '�������������=131321231',
            '����������=��� 7777777777 ���� ���������',
            '����������1=���� ���������',
            '������������������=22222810222222222222',
            '��������������1=���������� ����"���������������" ���',
            '��������������2=�. ������',
            '�������������=040001002',
            '�����������������=',
            '����������=������',
            '�����������������=�� �������� ������� ���',
            '�����������=4',
            '���������=01',
            '��������������'
]


file_counter = 0
number = 0

def new_file(user_info, PREFIX, DOCUMENT):# �� ���� ���������� � ������������ � 2 �������
    #amount = int(input('Amount of Pay Rolls in Doc:'))
    global amount
    global file_counter
    file_counter += 1
    f = open("C:\App\Files\Python\Testing/PayRollsDoc/PayRollsDoc%i.csv" % file_counter, "w+")
    for i in range(0, len(PREFIX)):#������ �� ������� �������� � ����� ��������� key, ��� ����������� ��������
        line = PREFIX[i]
        if "key" in line:# ��� ���������� �������� ������, � ����������������� ������ ������������ ������� ����/�����
            line2 = line.split("=")[1]
            line4 = line2.split(':')[1]
            if line4 =='date':
                f.write(line.split("=")[0]+'='+curr_date+'\n')
            elif line4 == 'time':
                f.write(line.split("=")[0]+'='+curr_time+'\n')
        else:
            f.write(PREFIX[i]+'\n')
    for j in range(0, amount):# ���-�� ��������� ��������� �������� ���������� amount
        global number
        number += 1#���������� �������� �������� ��� �����
        for k in range(0, len(DOCUMENT)):#������ �� ������� ����.��������� � ����� ��������� key, ��� ����������� ��������
            line = DOCUMENT[k]
            if "number" in line:# ������ �� ����� ����.���������
                line2 = line.split("=")[1]
                f.write(line.split("=")[0]+'='+str(number)+'\n')

            elif "key" in line:#������ key-��������(��� � ��)
                #line.split("=")
                line2 = line.split("=")[1]
                #line2.split(":")
                dictkey = line2.split(":")[1]
                if dictkey in dictCustom.keys():
                    f.write(line.split("=")[0]+'='+str(dictParams[user]+'\n'))#!!!!!!ne polniy code

            else:
                f.write(line+'\n')



new_file(3,PREFIX,DOCUMENT)










