k=0
for N in range(1,100000):
    N2=bin(N)[2:]
    if N%2==0:
        N2=N2+(bin(N2.count('1'))[2:])
    else:
        N2='1'+N2+'00'
    if 500<= (int(N2,2))<= 700:
        k+=1
print(k)        
