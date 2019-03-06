#1
class Pesan(object):
    def __init__(self,pesan):
        self.data=pesan
    
    def apakahTerkandung(self,kata):
        return kata in self.data

    def hitungKonsonan(self):
        v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        konsonan=0
        for i in self.data:
            if i in v:
                konsonan+=1
        return konsonan
    def hitungVokal(self):
        v="aiueoAIUEO"
        vokal=0
        for i in self.data:
            if i in v:
                vokal+=1
#2
class Manusia(object):
    def __init__(self,nama):
        self.nama=nama
    def ucapkansalam(self):
        print("Assalamu alaikum, Namaku",self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
    def olahraga(self,s):
        print("saya baru berolahraga",s)
    def mengalikandengandua(self,n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uangSaku=us
        #4
        #self.listkuliah=[]
    def __str__(self):
        a=self.nama
        b=", NIM "+self.NIM
        c=", Tinggal di "+ self.kota
        d=", Uang saku Rp "+ str(self.uangSaku)+" per bulan"
        return a+b+c+d    
    def ambilnama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilkotatinggal(self):
        return self.kota
    def ambiluangsaku(self):
        return self.uangSaku
    def perbaruikotatinggal(self,kota):
        self.kota=kota
    def tambahuUangSaku(self,tambahan):
        self.uangSaku+=tambahan
    #def ambilkuliah(self,namakuliah):
    #    self.listkuliah
#3
b=input("masukan nama mahasiswa: ")
c=input("masukan NIM mahasiswa: ")
d=input("masukan kota tempat Tinggal mahasiswa: ")
e=input("masukan Uang Saku mahasiswa: ")
f=Mahasiswa(b,c,d,e)

6#
class SiswaSMA(Manusia):
    def __init__(self,nama,NIS,kota,us):
        self.nama=nama
        self.NIS=NIS
        self.kota=kota
        self.uangSaku=us
    def __str__(self):
        a=self.nama
        b=", NIS "+self.NIS
        c=", Tinggal di "+ self.kota
        d=", Uang saku Rp "+ str(self.uangSaku)+" per bulan"
        return a+b+c+d

