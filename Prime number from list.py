l1=[3,7,6,9,5,6,2,4]

c=0

for i in l1:
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
        if(f==0):
            c+=1
            print("Prime no=",i)

print("Total=",c) 
