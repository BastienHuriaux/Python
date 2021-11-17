from ex4 import est_premier

a=True
c=1
while(a == True):
    b=pow(2,pow(2,c))+1
    a=est_premier(b)
    c+=1
print("Le premier nombre non premier de Fermat est:",b)

c=0
d=int(input("Entrez un nombre : "))

while(a==False):
    c+=1
    a=est_premier(d+c)
print("Le premier nombre premier après ",d," est ",d+c)

a=False
e=False
c=0
d=int(input("Entrez un nombre : "))
while(e==False):
    c+=1
    a=est_premier(d+c)
    if(a==True):
        e=est_premier(d+c+2)
print("Le premier couple de nombre premiers jumeaux après ",d," sont ",d+c," et ",d+c+2)


a=False
e=False
c=0
d=int(input("Entrez un nombre : "))
while(e==False):
    c+=1
    a=est_premier(d+c)
    if(a==True):
        e=est_premier(2*(d+c)+1)
print("Le premier nombre premier de Germain après ",d," est ",d+c)



