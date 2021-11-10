
p = int(input("Entrez un entier : "))
d=int(pow(p,0.5))

for i in range(2,d+1):
    a = p//i
    if(p%i == 0):
        print(p," = ",i," x ",a," : False")
        break
else:
    print(p," : True")