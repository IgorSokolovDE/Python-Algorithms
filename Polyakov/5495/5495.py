sumXY=100000000000000
for x in range(1,22):
    for y in range(0,13):
        oper=(x*22**4+2*22**3+3*22**2+x*22+5)-(6*13**4+7*13**3+y*13**2+9*13+y)
        if abs(oper)%57==0:
            if sumXY>(x+y):
                sumXY=(x+y)
                OP=oper
print(OP//57)                
