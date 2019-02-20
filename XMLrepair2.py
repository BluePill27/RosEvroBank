# -*- coding: utf-8 -*-

import sys
import os
import copy
from xml.etree import ElementTree as ET

if __name__ == "__main__":
    # correct input check
    if len(sys.argv) != 5:
        print("Wrong input format! - Not enough arguments passed.")
        print('example:"-folder c:\\xmls -out c:\\xmls\out"')
        sys.exit(1)
    else:
        if sys.argv[1] != '-folder' or sys.argv[3] != '-out':
            print("Wrong input format!")
            print('example:"-folder c:\\xmls -out c:\\xmls\out"')
            sys.exit(1)
        elif os.path.exists(sys.argv[2]) != True:
            print("Wrong input format!")
            print('No such directory:', sys.argv[2])
            sys.exit(1)
        elif os.path.exists(sys.argv[4]) != True:
            print("Wrong input format!")
            print('No such directory:', sys.argv[4])
            sys.exit(1)

        folder = sys.argv[2]#"C:\\#CVS\\QA.Load_Testing\\correqts\\py\\xmls"
        out = sys.argv[4]
        fileCount = 1000000
        # Get list of XML files
        for d_root, dirs, files in os.walk(folder): #get file list
            fileList = files
            break # Breaking iteration for next subfolders

        for file in fileList: # now edit only forst 10 files
            if ".xml" in file:
                print("processing %s" % file)
                if fileCount < 1: break # break process of parsing xml's

                tree = ET.parse( "%s\\%s" % (folder, file) )
                root = tree.getroot()
                print("root: ", root)

                # Replace current node <ServicePacks> to <ServicePacks><ServPackName>CRQTS. STANDART</ServPackName></ServicePacks>
                nsmap = {'ns' : "http://bssys.com/abs/model/client"}
                node = root.find(".//ns:ServicePacks", namespaces = nsmap)
                if node: # Remove all child elements & add <ServPackName>CRQTS. STANDART</ServPackName>
                    print("node %s" % node)
                    node.clear()
                    child = ET.fromstring("<ServPackName xmlns='http://bssys.com/abs/model/client'>CRQTS. STANDART</ServPackName>")
                    node.insert(0, child)
                    print(ET.tostring(node))

                # Add enother unic SUB element <Account> to <OrgData>
                accounts = root.find(".//ns:OrgData/ns:Accounts", namespaces = nsmap)
                acc = list(accounts)
                new_acc = copy.deepcopy(acc[0]) # make copy of first acc

                acc_num = new_acc.find(".//ns:Num", namespaces = nsmap)
                acc_num.text = str(int(acc_num.text) + 10000000000) # Add one 10 billion to account number
                accounts.append(new_acc)

                fileCount -= 1 #decrement
                print ("fileCount %s" % fileCount)

                tree.write( "%s\\_%s" % (out, file), encoding='utf-8')
