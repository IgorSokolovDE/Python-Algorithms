def Gut(x,y):
    if ((x//1000)+(y//1000))==((x%10)+(y%10)):
        return True
    else:
        return False
A=[int(x) for x in open('17-316.txt')]
AVG=sum(A)/len(A)
k3=0
MaxSum3=0
for i in range(len(A)-2):
    if ((A[i]+A[i+1]+A[i+2])/3)>AVG:
        if Gut(A[i],A[i+1]) or Gut(A[i],A[i+2])or Gut(A[i+2],A[i+1]):
            k3+=1
            MaxSum3=max(MaxSum3,(A[i]+A[i+1]+A[i+2]))
print(k3,MaxSum3)            
        
