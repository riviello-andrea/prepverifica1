import random
x=random.randint(1,1000)
y=random.randint(1,1000)
z=random.randint(1,1000)
if x<y and x<z:
    print(x)
    if y<z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y<z:
    print(y)
    if z<x:
        print(z)
        print(x)
    else:
        print(x)
        print(z)
else:
    print(z)
    if x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")
auto=["Ferrari", "Audi", "Lancia", "Mercedes", "Cupra"]
moto=["BMW", "KTM", "Ducati", "Aprilia"]
motocicli=auto+moto
motocicli.sort()
print(motocicli)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")
lista=[]
for i in range(50):
  lista.append(random.randint(1,1000))  
for x in lista:
    if x%2==0:
        lista.remove(x)
print(lista)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")
