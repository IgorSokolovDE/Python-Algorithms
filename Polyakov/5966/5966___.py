x10=0
while True:
    x10+=1
    x=x10
    x7=''
    while x>0:
        x7=str(x%7)+x7
        x//=7
    for centr in ['','0','1','2','3','4','5','6']:
        palindrom=(x7)+centr+(x7[::-1])
        Dec=int(palindrom,7)
        if Dec>(2023**3):
            break
        x3=''
        x=Dec
        while x>0:
            x3=str(x%3)+x3
            x//=3
        if x3==x3[::-1]:
            SDec=str(Dec)
            if (SDec[-1]=='0')and('2' in SDec):
                x8=oct(Dec)[2:]
                SumCifr8=0
                for sym8 in x8:
                    SumCifr8+=int(sym8)
                print(Dec, SumCifr8)   
        
