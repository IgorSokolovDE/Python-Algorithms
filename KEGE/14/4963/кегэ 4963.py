naschli=False
for y in range(0,17):
    for x in range(0,15):
        ch=(1*15**4+2*15**3+3*15**2+x*15**1+5*15**0)+(6*17**3+7*17**2+y*17**1+9*17**0)
        if ch%131==0:
            print(ch//131)
            naschli=True
            break
    if naschli:
            break    
