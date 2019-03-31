#Nama   : Yusuf anwar
#NIM    : L200170086
#Kelas  : C
#Modul  : 5
#----------------------------------------------------------------------------------------------------------------------


from Modul_2 import Mahasiswa as Mhs

######1#######
a=Mhs("Yusuf","L200171100","Boyolali",2000)
b=Mhs("Anwar","L200170065","Solo",3000)
c=Mhs("Eb","L200170001","Boyolali",2500)
d=Mhs("Ya","L200170012","Boyolali",2000)
e=Mhs("Ye","L200170004","Boyolali",1000)
f=Mhs("Be","L200170009","Boyolali",1000)
g=Mhs("Ac","L200170186","Boyolali",1000)
h=Mhs("Oanr","L200170486","Boyolali",1000)
i=Mhs("Oes","L200170096","Boyolali",1000)
h=[a,b,c,d,e,f,g,h,i]

def bubble_sort(daftar):
    b=len(daftar)-1;
    while b!=0:
        for i in range(0, b):
            if daftar[i].NIM>daftar[i+1].NIM:
                a=daftar[i]
                daftar[i]=daftar[i+1]
                daftar[i+1]=a
        b-=1
def selection_sort(daftar):
    for i in range(0,len(daftar)):
        terkecil = i
        for j in range(i+1,len(daftar)):
            if daftar[terkecil].NIM>daftar[j].NIM:
                terkecil=j
        if terkecil!=i:
            terbesar=daftar[i]
            daftar[i]=daftar[terkecil]
            daftar[terkecil]=terbesar

selection_sort(h)
for i in range(0,len(h)):
    print(h[i])



######2#######
A=[1,2,3,4,5,7,9,11,13]
B=[2,4,6,8,10,12,14,16]

def gambungkan(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and i<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j += 1
    while i<len(a):
        c.append(a[i])
        i += 1
    while j<len(b):
        c.append(b[j])
        j += 1
    return c
C=gambungkan(A,B)
print(C)

######3#######
def bubble_sort(daftar):
    b=len(daftar)-1;
    while b!=0:
        for i in range(0, b):
            if daftar[i]>daftar[i+1]:
                a=daftar[i]
                daftar[i]=daftar[i+1]
                daftar[i+1]=a
        b-=1
def selection_sort(daftar):
    for i in range(0,len(daftar)):
        terkecil = i
        for j in range(i+1,len(daftar)):
            if daftar[terkecil]>daftar[j]:
                terkecil=j
        if terkecil!=i:
            terbesar=daftar[i]
            daftar[i]=daftar[terkecil]
            daftar[terkecil]=terbesar
def insertion_sort(daftar):
    n=len(daftar)
    for i in range(0,n):
        nilai=daftar[i]
        pos=i
        while pos>0 and nilai<daftar[pos-1]:
            daftar[pos]=daftar[pos-1]
            pos-=1
        daftar[pos]=nilai

from time import time as detak
from random import shuffle as kocok
k=[range(1,6001)]
kocok(k)
u_bub=k[:]
u_sel=k[:]
u_ins=k[:]
aw=detak()
bubble_sort(u_bub)
ak=detak()
print("buble %g detik" %(ak-aw))
aw=detak()
selection_sort(u_sel)
ak=detak()
print("selection %g detik" %(ak-aw))
aw=detak()
insertion_sort(u_ins)
ak=detak()
print("insertion %g detik" %(ak-aw))