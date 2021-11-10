

def syracuse(n):
    a=n
    while(a!=0):
        if(a%2==0):
            a = a/2
        else:
            a = a*3+1
    print(a)
    return

syracuse(15)
