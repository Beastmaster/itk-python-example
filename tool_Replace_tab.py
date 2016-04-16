'''
Author: Qin Shuo
Date:   2016/04/16
Description:
    Replace 'tab' key with 4 whitespace
'''

import sys
import string



def replace_tab(file_name,index):
    print "option 1: replace 'tab \t' with 4 white space"
    print "option 2: replace 'self.Event' with 'self.e_Event'"

    # create a file handle
    fp = open(file_name,'r')
    
    if index == '1':
        content = fp.read()
        new_content = content.replace('\t','    ')
    elif index == '2': 
        content = fp.readlines()
        new_content = ""
        for line in content:
            if line.rfind("self.")!=-1:
                id = line.rfind("self.")+len("self.")
                nline = line[:id]+"e_"+line[id:]
            else:  
                nline = line
            new_content = new_content+nline
    fp.close()

    ind = file_name.rfind('.')
    new_name = file_name[:ind]+"new_"+file_name[ind:]
    print "New file name: "+new_name
    fp2 = open(new_name,'w+')
    fp2.write(new_content)
    fp2.close()


if __name__ == '__main__':
    #file_name = sys.argv[1]
    if len(sys.argv)<3:
        print "no enough parameters..."
        print "file,[selection]"
        exit()
    else:
        file_name = sys.argv[1]
        print "replacing: "+ file_name
        replace_tab(file_name,sys.argv[2])
    

