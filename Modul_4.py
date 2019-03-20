from Modul_2 import Mahasiswa as Mhs

a=Mhs("Yusuf","L200170086","Boyolali",2000)
b=Mhs("Anwar","L200170065","Solo",3000)
c=Mhs("eb","L200170086","Boyolali",2500)
d=Mhs("Ya","L200170086","Boyolali",2000)
e=Mhs("Ye","L200170086","Boyolali",1000)
e=[a,b,c,d,e]
#1
def cariasalkota(himpunan,kota):
    nilaikembali=[]
    for i in range(0,len(himpunan)):
        if himpunan[i].kota==kota:
            nilaikembali.append(i)
    return  nilaikembali
#2
def cariuangsakuterkecil(himpunan):
    terkecil=himpunan[0]
    for i in range(1, len(himpunan)):
        if terkecil.uangSaku>himpunan[i].uangSaku:
            terkecil=himpunan[i]
    return terkecil
#3
def cariuangsakuterkecil1(himpunan):
    terkecil = [himpunan[0]]
    for i in range(1, len(himpunan)):
        if terkecil[0].uangSaku > himpunan[i].uangSaku:
            terkecil.clear()
            terkecil.append(himpunan[i])
        elif terkecil[0].uangSaku == himpunan[i].uangSaku:
            terkecil.append(himpunan[i])
    return terkecil

#4
def uangsakukurangdari(himpunan,pembanding):
    hasil=[]
    for i in range(0, len(himpunan)):
        if himpunan[i].uangSaku<pembanding:
            hasil.append(himpunan[i])
    return hasil
e=uangsakukurangdari(e,2500)
for i in range(0,len(e)):
    print(e[i])

from Modul_3 import Node
#5
a=Node(10,Node(20,Node(30,Node(40,Node(50)))))
def cari(mulai,target):
    if mulai.data!=target:
        if mulai.next!=None:
            return cari(mulai.next,target)
        else:
            return None
    return mulai.data
#6
def BinSe(himpunan,target):
    low=0
    high=len(himpunan)-1
    while low!=high:
        mid=(high+low)//2
        if himpunan[mid]==target:
            return mid
        elif target<himpunan[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
#7
def BinSe(himpunan,target):
    hasil=[]
    low = 0
    high = len(himpunan) - 1
    while low != high:
        mid = (high + low) // 2
        if himpunan[mid] == target:
            break
        elif target < himpunan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    for i in range(low,high):
        if target==himpunan[i]:
            hasil.append(i)
    return hasil