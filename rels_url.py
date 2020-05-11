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
            if not data.startswith ('"http://schemas.openxmlformats.org/') \
                and not data.startswith('"http://schemas.microsoft.com/') \
                and not data.startswith('"http://purl.org/') \
                and not data.startswith('"http://www.w3.org/'):
                    print(data)
        continue
zf.close()

