A=[int(x) for x in open('17-324.txt')]
Sum=0
kol=0
for x in A:
    if x%37!=0:
        Sum+=x
        kol+=1
AVGne37=Sum/kol
k3=0
MaxSum3=0
for i in range(len(A)-2):
    if min(A[i],A[i+1],A[i+2])>AVGne37:
        Sum3=A[i]+A[i+1]+A[i+2]
        B=bin(Sum3)[2:]
        if B==B[::-1]:
            k3+=1
            MaxSum3=max(MaxSum3,Sum3)
print(k3,MaxSum3)            
