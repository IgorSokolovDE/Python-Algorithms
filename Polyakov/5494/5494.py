for y  in range(17):
    for x in range(15):
        R=(1*15**4)+2*15**3+3*15**2+x*15+5
        B=6*17**3+7*17**2+y*17+9
        if (R+B)%131==0:
            print((R+B)//131,y)
            iii=input()
            
        
