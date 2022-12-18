for k5 in range(301,100000000000000000000000000):
    S='5'*k5
    while ('555' in S)or('888' in S):
        S=S.replace('555','8',1)
        S=S.replace('888','55',1)
    if (len(S)==2)and(S.count('5')==1)and(S.count('8')==1):
        print(k5)
        break
