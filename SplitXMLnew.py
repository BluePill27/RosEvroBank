f = open("C:\\App\\Files\\Python\\Split XML\\клиенты за август xml(SHORT).txt", "r")
curr_number = 1
line = f.readline()
while line:
    write_file = open("C:\\App\\Files\\Python\\Split XML\\TestResults\\XML%i.xml" % curr_number, 'w', encoding = "utf-8")
    curr_number+=1
    write_file.write(line)
    line = f.readline()