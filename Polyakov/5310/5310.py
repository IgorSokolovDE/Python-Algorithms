f=open('26-87.txt')
N=int(f.readline())
Pixels=[]
for i in range(N):
    
    s=f.readline()
    a=s.split()
    Rad=int(a[0])
    Pos=int(a[1])
    color=a[2]
    Pixels.append([Rad,Pos,color])
Pixels.sort()
Vsego=0
NumRada=0
kolPixVRadu=0
MaxkolPixVRadu=0
NumRadaMaxkolPixVRadu=0

for i in range(N-3):
    if Pixels[i][2]=='#00FF00':
        Rad=Pixels[i][0]
        Pos=Pixels[i][1]
        KolToRight=0
        for j in range(3):
            if Pixels[i+j+1][2]=="#0000FF":
                if Rad==Pixels[i+j+1][0]:
                    if Pos+j+1==Pixels[i+j+1][1]:
                        KolToRight+=1
        KolToLeft=0
        for j in range(3):
            if Pixels[i-j-1][2]=="#0000FF":
                if Rad==Pixels[i-j-1][0]:
                    if Pos-j-1==Pixels[i-j-1][1]:
                        KolToLeft+=1
        if (KolToLeft==3)and(KolToRight==3):
            if Rad==NumRada:
                kolPixVRadu+=1
            else:
                if kolPixVRadu>=MaxkolPixVRadu:
                    MaxkolPixVRadu=kolPixVRadu
                    NumRadaMaxkolPixVRadu=NumRada
                NumRada=Rad
                kolPixVRadu=1
            Vsego+=1
print(Vsego,  NumRadaMaxkolPixVRadu)          
                                      
