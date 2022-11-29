from functools import reduce
def soma(x,y):
    return x+y
def multi(x,y):
    return x*y
s = soma(2,6)
m = multi(6,8)
print(s)
print(m)

print(f"A soma das funções é {soma(s,m)}")


def dobro(z):
    return z*2
s = 2
print(dobro(s))

#fução map
l = [5,6,4,9,7,8,1,5]
dobro2 = map(dobro,l)
dobro2 = list(dobro2)
print(dobro2)

#função reduce

soma = reduce(soma,l)
print(soma)

#função zip

list1 = [1,2,3,4,5,6]
list2 = ['fellipe','leticia','casamento','mulher perfeita','pouxa','caramba']
list3 = []
for n,nome in zip(list1,list2):
    print(n,nome)
#def dobro 3

def dobrooo(h):
    if h%2==0:
        return h
list3 = [h%2 for h in list1]

def calcular(*args):
    r = sum(args)
    for i in args:
        r +=i
    return r

print(calcular(1,4,5))