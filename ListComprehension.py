x = [1,2,3,4,5]
y = [i**2 for i in x] #elevar ao cubo
z = [i for i in x if i%2 ==0]#pares e impares
print(z)

#função enumarate

for i in range(len(x)):
    print(i, x[i])

for i,numero in enumerate(x):
    print(i,numero)