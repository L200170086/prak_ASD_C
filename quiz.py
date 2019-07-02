class quizone(object):
    def __init__(self,data=[]):
        self.items=data
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def __getitem__(self, item):
        return self.items[item]
    def __setitem__(self, key, value):
        self.items[key]=value
    def mergesort(self):
        b = len(self.items)
        if b > 1:
            a = b // 2
            y = quizone(self.items[:a])
            z = quizone(self.items[a:])
            y.mergesort()
            z.mergesort()
            i = 0;
            j = 0;
            k = 0
            while i < len(y) and j < len(z):
                if y[i] < z[j]:
                    self.items[k] = y[i]
                    i = i + 1
                else:
                    self.items[k] = z[j]
                    j = j + 1
                k = k + 1
            while i < len(y):
                self.items[k] = y[i]
                i = i + 1
                k = k + 1
            while j < len(z):
                self.items[k] = z[j]
                j = j + 1
                k = k + 1
    def peek(self):
        assert not self.isEmpty(),"stack kosong. tidak bisa diintip"
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(),"stack kosong. tidak bisa di-pop"
        return self.items.pop()
    def push(self,data):
        print(data+" telah di push")
        self.items.append(data)
a=["Yusuf","Bintang","Habib","Dimas","Lutfi","Yusinta","Yulia","Laras","Herda","Lori","Hada"]
#1
b=quizone(a)
b.mergesort()
print(a)
print("\n")

#2
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
b.push("Deni")
b.push("Dean")
b.push("Doni")
print(b.pop())
b.push("Bean")
print(b.pop())
print(b.pop())
print(b.pop())
print("\n")
#3
class simpulpohonbiner(object):
    def __init__(self,data):
        self.data=data
        self.kiri=None
        self.kanan=None
    def depth(self,data):
        if self.kiri!=None and self.kanan!=None:
            if self.kiri.depth(data)!=None and self.kanan.depth(data)!=None:
                if self.kiri.depth(data)>self.kanan.depth(data):
                    return self.kiri.depth(data)+1
                return self.kanan.depth(data)+1
            if self.kiri.depth(data)!=None:
                return self.kiri.depth(data)+1
            if self.kanan.depth(data)!=None:
                return self.kanan.depth(data)+1
        if self.kiri!= None:
            if self.kiri.depth(data)!=None:
                return self.kiri.depth(data)+1
        if self.kanan!= None:
            if self.kanan.depth(data) != None:
                return self.kanan.depth(data)+1
        if self.data==data:
            return 0
        return None
    def height(self):
        if self.kiri==None and self.kanan==None:
            return 1
        if self.kiri==None:
            return self.kanan.height() + 1
        if self.kanan==None:
            return self.kiri.height() + 1
        if self.kanan.height()>self.kiri.height():
            return self.kanan.height()+1
        return self.kiri.height()+1


ab=simpulpohonbiner("X")
ab.kiri=simpulpohonbiner("D")
ab.kiri.kanan=simpulpohonbiner("N")
ab.kiri.kanan.kiri=simpulpohonbiner("S")
ab.kiri.kanan.kiri.kiri=simpulpohonbiner("W")
ab.kiri.kanan.kiri.kanan=simpulpohonbiner("Q")
ab.kanan=simpulpohonbiner("Y")
ab.kanan.kanan=simpulpohonbiner("Q")
ab.kanan.kanan.kiri=simpulpohonbiner("A")
ab.kanan.kanan.kanan=simpulpohonbiner("V")

print("height " +str(ab.height()))
print("depth 'N' "+str(ab.depth("N")))
print("lenght " + str(3))

print("\n")
#4
def preorder(ac):
    if ac != None:
        print(ac.data)
        preorder(ac.kiri)
        preorder(ac.kanan)

preorder(ab)
print("\n")
def inorder(ac):
    if ac !=None:
        inorder(ac.kiri)
        print(ac.data)
        inorder(ac.kanan)

inorder(ab)
import mysql.connector