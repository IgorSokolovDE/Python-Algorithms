A=[int(x) for x in open("17-353.txt")]
kPar=0
MaxSum=0
srznach=(max(A)+min(A))/2
for i in range(len(A)//2):
    ch1=A[i]
    ch2=A[-(i+1)]
    if ((ch1<srznach)and(ch2>srznach))or((ch1>srznach)and(ch2<srznach)):
        kPar+=1
        MaxSum=max(MaxSum,(ch1+ch2))
print(kPar, MaxSum)      
