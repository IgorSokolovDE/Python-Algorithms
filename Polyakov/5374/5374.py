A=[int(x) for x in open('17-340.txt')]
Sum22=0
kol22=0
for x in A:
    if x%22==0:
        Sum22+=x
        kol22+=1
srA22=Sum22/kol22
k2=0
maxSum2=0
for i in range(len(A)-1):
    x8=oct(A[i])[2:]
    y8=oct(A[i+1])[2:]
    maxCifrx8=0
    minCifrx8=8
    for cifr in x8:
        maxCifrx8=max(maxCifrx8,int(cifr))
        minCifrx8=min(minCifrx8,int(cifr))
    NumMaxX=x8.index(str(maxCifrx8))
    x8=x8[::-1]
    NumMinX=len(x8)-x8.index(str(minCifrx8))
    maxCifry8=0
    minCifry8=8
    for cifr in y8:
        maxCifry8=max(maxCifry8,int(cifr))
        minCifry8=min(minCifry8,int(cifr))
    NumMaxY=y8.index(str(maxCifry8))
    y8=y8[::-1]
    NumMinY=len(y8)-y8.index(str(minCifry8))
    print(x8,NumMinX,NumMinX, y8, NumMinY,NumMinY)
    iii=input()
    if (NumMinX<NumMinX)and (NumMinY<NumMinY):
        k2+=1
        maxSum2=max(maxSum2,(A[i]+A[i+1]))
print(k2,maxSum2)                    
