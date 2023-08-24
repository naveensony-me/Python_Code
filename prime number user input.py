count=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
  if n%i==0:
    count+=1
    
if count==2:
    print("Prime Number",n)
else:
    print("Not Prime number",n)