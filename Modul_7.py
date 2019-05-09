#Nama   : Yusuf anwar
#NIM    : L200170086
#Kelas  : C
#Modul  : 7
#----------------------------------------------------------------------------------------------------------------------
import re

a=open("indonesia", "r")
b=a.read()
a.close()

a=open("KEI.html", "r",encoding="latin1")
c=a.read()
a.close()

#1
pola1=r"me\w+"
tampil1=re.findall(pola1,b)
#2
pola2=r"di\w+"
tampil2=re.findall(pola2,b)
#3
pola3=r"di \w+"
tampil3=re.findall(pola3,b)
#4
f=open('KEI.html','r',encoding='latin1')
text=f.read()
pola4=r"([\w ]+)</a></td>\n<td>([\w.]+)"
tampil4=re.findall(pola4,text)
print(tampil1)
print(tampil2)
print(tampil3)
print(tampil4)