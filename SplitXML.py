f = open("C:\\App\\Files\\Python\\Split XML\\kek.csv", "r")
curr_number = 1
line = f.readline()
while line:
    split_line = line.split(';')
    if (split_line[0]+';') == str(str(curr_number) +';'):
        write_file = open("C:\\App\\Files\\Python\\Split XML\\Result(40)\\XML%i.xml" % curr_number, 'w', encoding = "utf-8")
        #write_file.write(str(str(curr_number) +';'))
        for part in range(1, len(split_line)):
            if part == len(split_line)-1:
                split_again_line = split_line[part].split('""')
                for part2 in range(0, len(split_again_line)):
                    if part2 == len(split_again_line)-1:
                        write_file.write(split_again_line[part2].rstrip('"\n')+'\n')
                    else:
                        write_file.write(split_again_line[part2]+'"')
            elif part == 1:
                split_again_line = split_line[part].split('""')
                for part2 in range(0, len(split_again_line)):
                    if part2 == 0:
                        tmp = str(split_again_line[part2]+'"').lstrip('"')
                        write_file.write(tmp)
                        print(tmp)
                    elif part2 == len(split_again_line)-1:
                        write_file.write((split_again_line[part2] + ';'))
                    else:
                        write_file.write(split_again_line[part2] + '"')
            else:
                split_again_line = split_line[part].split('""')
                for part2 in range(0, len(split_again_line)):
                    if part2 == len(split_again_line)-1:
                        write_file.write((split_again_line[part2] + ';'))
                    else:
                        write_file.write(split_again_line[part2]+'"')
        curr_number += 1
        print((split_line[0])+';')
    line = f.readline()

