a=int(input("Enter no=  "))
o=a
c=0
while a>0:
    c=c+(a%10)*(a%10)*(a%10)
    a=a//10
if c==o:
    print("amstrong")
else:
    print("not amstrong")
