for x10 in range(16):
    x16=hex(x10)[2:]
    y10=int(('8569'+x16),16)+int(('12'+x16+'48'),16)
    y8=oct(y10)[2:]
    kolChCifr=y8.count('0')+y8.count('2')+y8.count('4')+y8.count('6')
    if kolChCifr<=2:
        Sy8=y8
print(Sy8)        
