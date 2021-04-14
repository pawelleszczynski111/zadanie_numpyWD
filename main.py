import numpy as nump
# zad1

a = nump.arange(4,21*4,4)
print(a)

# # zad2
#
# b = nump.array([1,2,3,4,5],dtype=float)
# print(b)
# print(b.dtype)
# c = b.copy().astype('int32')
# b[0]=3
# print(c)
# print(c.dtype)
#
# #zad3
#
# def ciag(n):
#     print(nump.array([2**x for x in range(n**2)]).reshape(n,n))
#
# print(ciag(5))
#
# tablica = nump.array([[1,2],[3,4],[5,6]])
# print(tablica.reshape(2,3))
#
# lista = nump.arange(6).reshape(3,2)
# print(lista)
# lista = nump.arange(2*3).reshape(2,3)
# print(lista)
#
# def generuj(n,p):
#        return  nump.logspace(2,4,base=2,num=16)
#
# print(generuj(2,4))
#
#
# def generuj_wektor(n):
#     return nump.diag(nump.linspace(n,0,n),2)
#
# print(generuj_wektor(5))