from ex4 import est_premier

a=True
c=1
while(a == True):
    b=pow(2,pow(2,c))+1
    a=est_premier(b)
    c+=1
print("Le premier nombre non premier de Fermat est:",b)