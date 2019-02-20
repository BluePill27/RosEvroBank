# -*- coding: utf-8 -*-
import sys
import os
import re

#correct input check
if len(sys.argv) != 5:
    print("Wrong input format! - Not enough arguments passed.")
    print('example:"-file c:\\xmls\\ex.xml -out c:\\xmls\out"')
    sys.exit(1)
else:
    if sys.argv[1] != '-file' or sys.argv[3] != '-out':
        print("Wrong input format!")
        print('example:"-file c:\\xmls -out c:\\xmls\out"')
        sys.exit(1)
    elif os.path.exists(sys.argv[2]) != True:
        print("Wrong input format!")
        print('No such file:', sys.argv[2])
        sys.exit(1)
    elif os.path.exists(sys.argv[4]) != True:
        print("Wrong input format!")
        print('No such directory:', sys.argv[4])
        sys.exit(1)
file = sys.argv[2] #"C:\\#CVS\\QA.Load_Testing\\correqts\\py\\ex.xml"
out = sys.argv[4] #"C:\\#CVS\\QA.Load_Testing\\correqts\\py\\ex.out_%s.xml"

file_out_counter = 1
common_id_counetr = 20180916
account_counetr = 40702810201000361880

for findex in range (file_out_counter, 5):
    with open(file, 'r', encoding="utf-8") as f:
        f_out = open(out + "\\ex.out_%s.xml" % str(findex).zfill(6), 'a', encoding="utf-8")
        #with open("C:\\#CVS\\QA.Load_Testing\\correqts\\py\\ex.out.xml", 'a', encoding="utf-8") as fw:
        for line in f:
            mstr = line
            if "20180817_1_1" in line: # Нашли волшебную строку
                mstr = line.replace("20180817_1_1", "%s_1_1" % str(common_id_counetr))
                print(mstr)
            if "<Num>" in line:
                print("<Num> found")
                mstr = re.sub("<Num>\d+</Num>", "<Num>%s</Num>" % str(account_counetr), line)
                print (mstr)
            f_out.write(mstr)
        f_out.close()
    common_id_counetr += 1
    account_counetr += 1