'''
Author: Qin Shuo
Date:   2016/04/16
Description:
    Replace 'tab' key with 4 whitespace
'''

import sys
import string



def replace_tab(file_name):
    # create a file handle
    fp = open(file_name,'r')
    content = fp.read()
    fp.close()

    new_content = content.replace('\t','    ')

    ind = file_name.rfind('.')
    new_name = file_name[:ind]+"new_"+file_name[ind:]
    print "New file name: "+new_name
    fp2 = open(new_name,'w+')
    fp2.write(new_content)
    fp2.close()


if __name__ == '__main__':
    #file_name = sys.argv[1]
    if len(sys.argv)<2:
        print "no input file"
        exit()
    else:
        file_name = sys.argv[1]
        print "replacing: "+ file_name
        replace_tab(file_name)
    

