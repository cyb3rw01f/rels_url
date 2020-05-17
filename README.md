# rels_url
Office 2007+ Relational links URL extractor  
rels_url is a script to parse post 2003 MS Office documents (e.g. docx, xlsx), to reveal URLs  

Reveal URLS in the relationship files, .rels files.

**To Use:**  
rels_url.py  file.docx

**The output will list the folder and file the URL is located. Sample Output:**  
 C:\Users\cyb3rw01f>rels_url.py D:\rels_docx

_rels/.rels

word/_rels/document.xml.rels

word/_rels/settings.xml.rels  
"https://sample.com/sample1/sample2/file.exe"

customXml/_rels/item1.xml.rels

customXml/_rels/item2.xml.rels

customXml/_rels/item3.xml.rels

customXml/_rels/item4.xml.rels
