a=5
b=0
c=1
r=b+c
for x in range(0,a):
    for y in range(0, x+1):
        print(str(r) + "",end="")
        r=b+c
        b=c
        c=r
    print()    
