import os
import zipfile
import re


def msgidcount(dirt,parser):
    dirt+="\etc\devices"
    parser_path= os.path.join(dirt,parser)
    print(parser_path)
    for root,directory,filename in os.walk(parser_path):
        print(root)
        for i in filename:
            print(i)
            if i.endswith('.xml'):
                print(i)
                finame="%s\%s"%(root,i)
                print(finame)
                with open(finame,'r')as rd:
                    rea=rd.read()
                    print(rea)
                    msgid = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"', rea, flags=re.DOTALL)
                    print(msgid)
                    print(len(msgid))
                    return (len(msgid))







if __name__=="__main__":
    parser_location = "C:\CICD\content-qe-tools\content-cdp\output"
    parser_name = 'winevent_nic'

    count= msgidcount(parser_location,parser_name)

