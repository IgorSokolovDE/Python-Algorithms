for N in range(13,1000000000):
    s=str(N)
    s2=''
    for s1 in s:
        s1_2=bin(int(s1))[2:]
        s1_2='0'*(4-len(s1_2))+s1_2
        if s1_2.count('1')%2==0:
            s1_2=s1_2+'0'
        else:
            s1_2=s1_2+'1'
        s2=s2+s1_2
        
    s2=s2+'0'
    s2=s2[2:]
    s2='1'+s2
    R=int(s2,2)
    if R==674890:
        print(N)
        break
