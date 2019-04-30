#Nama   : Yusuf anwar
#NIM    : L200170086
#Kelas  : C
#Modul  : 6
#----------------------------------------------------------------------------------------------------------------------


#from Modul_2 import Mahasiswa as Mhs

#kode merge sort
def mergesort(a):
    print("belah ",a)
    length=len(a)
    if length>1:
       mid=length//2
       separuhkiri=a[:mid]
       separuhkanan=a[mid:]
       
       mergesort(separuhkiri)
       mergesort(separuhkanan)

       i=0
       j=0
       k=0
       while i<len(separuhkiri) and j<len(separuhkanan):
           if separuhkiri[i]<separuhkanan[j]:
               a[k]=separuhkiri[i]
               i+=1
           else:
               a[k]=separuhkanan[j]
               j+=1
           k+=1
       while i<len(separuhkiri):
           a[k]=separuhkiri[i]
           i+=1
           k+=1
       while j<len(separuhkanan):
           a[k]=separuhkanan[j]
           j+=1
           k+=1
    print("gabung ",a)

a=[30,20,10,100,5,2,1,67,43]
mergesort(a)
print(a)
