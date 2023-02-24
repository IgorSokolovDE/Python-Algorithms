def F(n):
    if n<10:
        return 0
    else:
        return F(n//10)+((n//10)%10)-(n%10)
#for n in range(1,100000):
#    if F(n)==9:
#        print(n,F(n))
s=0
for x in range(0,9):
   s+=10**x
print(s)   
