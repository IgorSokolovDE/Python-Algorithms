f=open('26-91.txt')
N,D=map(int, f.readline().split())
boxs=[int(x) for x in f]
boxs.sort()
boxs=boxs[::-1]
Kont=0
SumSinglKont=0
while len(boxs)>0:
    if (boxs[0]+boxs[-1]) <=D:
        Kont+=1
        boxs.pop(-1)
        boxs.pop(0)
    else:
        SumSinglKont+=boxs[0]
        boxs.pop(0)
print(Kont,  SumSinglKont)      

    
