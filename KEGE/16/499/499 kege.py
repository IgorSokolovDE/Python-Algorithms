def F(n):
    if n<50:
        return n
    else:
        return 2*G(50-(n//2))
def G(n):
    if n>40:
        return 10
    else:
        return 30+F(n+600//n)
print(F(80))    
