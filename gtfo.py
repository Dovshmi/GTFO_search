import requests
from bs4 import BeautifulSoup
import sys
import os.path
import time
from alive_progress import alive_bar
from prettytable import PrettyTable

inputcheck=len(sys.argv)

if inputcheck > 1:
    path=sys.argv[1]
    pathcheck=os.path.isfile(path)
    if path == "--help":
        print("usage: python.py /path/to/file, --help for help menu")
    elif path == "-h":
        print("usage: python.py /path/to/file, --help or -h for help menu")
    elif pathcheck == False:
        print("usage: python.py /path/to/file, --help for help menu")
        print("the file that you wanted to check does not exist")
    file = open(path,'r')
    lines = file.readlines()
    file.close()
    linelen = len(lines)
    Big_list = []

    with alive_bar(linelen, title='Creating Wordlist',bar='blocks') as bar:
        for x in lines:
            file_check = x.split(" ")
            file_check2 = file_check[len(file_check)-1].split("/")
            file_check3 = file_check2[len(file_check2)-1]
            Big_list.append(file_check3)
            time.sleep(0.1)
            bar()
    
    print(" ")
    Biglen = len(Big_list)

    with alive_bar(Biglen,title='Searching In GTFO',bar='blocks') as bar2:
        head = []
        data = []
        data2=[]
        myTable = PrettyTable()
        f = -1
        wowcheck = 0
        urlist = []
        for i in Big_list:
            goodline = i.split('\n')
            goodline = goodline[0]
            url = 'https://gtfobins.github.io/gtfobins/'+goodline
            urlist.append(url)
            r = requests.get(url) 
            if r.status_code ==200:
                f = f+1
                head.append(goodline)
                soup = BeautifulSoup(r.content, 'html5lib')
                table = soup.find('h2', attrs = {'class':'function-name'})
                table2 = soup.findAll('h2', attrs = {'class':'function-name'})
                data = []
                lentable2 = -1
                data.append(url)
                for row in table2:
                    row = str(row)
                    row2 = row.split(">")
                    row3 = row2[len(row2)-2].split("<")
                    data.append(row3[0])
                if wowcheck < len(data):
                    wowcheck = len(data)

                data2.append(data)
            elif f == -1:
                print("No Exploits Found")
                sys.exit()
            
            bar2()
    data3 = []
    datalen= len(data2)
    print(" ")
    headnum = 0

    with alive_bar(datalen, title='Building De Table',bar='blocks') as bar3:
        for p in data2:
            if wowcheck > len(p):
                check = wowcheck - len(p)
                for t in range(check):
                    p.append("Null/Nothing")
            data3.append(p)
            time.sleep(0.1)
            bar3()
        for r in range(f+1):
            myTable.add_column(head[r],data3[r])

    file = open("GTFO_"+path,'w')
    file.write(myTable.get_string(title="GTFOWD"))
    file.close()
    time.sleep(1)
    print("")
    print(myTable)

else:
    print("usage: python.py /path/to/file, --help or -h for help menu")

