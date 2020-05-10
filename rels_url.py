import re
from zipfile import ZipFile
from sys import argv


myFile = str(argv[1])
zf = ZipFile(myFile, 'r')
getcont = zf.namelist()
for x in getcont:
    if ".rels" in x:
        content = zf.read(x)
        match = content.decode()
        url = re.findall('("http.*?")', match)
        print("")
        print(x)
        for data in url:
            print(data)
        continue
zf.close()
