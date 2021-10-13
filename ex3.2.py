b=0
c=0
d=0
e=0
g=0
h=0
for i in range(1,10000):
    n=i
    a=0
    r=0
    f=0
    Test=1
    while(n!=1):
        if(n%2 == 0):
            n=n/2
            r+=1
        else:
            n=n*3+1
            r+=1
        if(n>a):
            a=n
        if(n<i and Test == 1):
            f=r-1
    if(a>b):
        b=a
        c=i
    if(r>d):
        d=r
        e=i
    if(f>g):
        g=f
        h=i
    print("Pour n =",i,", le max est : ",a,", le temps de vol est : ",r,"et le temps de vol en altitude est :",f)
print("L'altitude maximale est :",b," pour n =",c)
print("Le temps de vol max est :",d," pour n =",e)
print("Le temps de vol max en altitude est :",g," pour n =",h)