for n in range(100,201):
    for m in range(100,201):
        for k in range(100,201):
            s='>'+'1'*k+'2'*m+'*'*n
            while ('>1' in s)or('>2' in s)or('>*' in s):
                if ('>1' in s):
                    s=s.replace('>1','111>',1)
                if ('>2' in s):
                    s=s.replace('>2','1>',1)
                if ('>*' in s):
                    s=s.replace('>*','%2*>',1)
            SumCifr=0
            for s1 in s:
                if (s1=='1')or(s1=='2'):
                    SumCifr+=int(s1)
            if SumCifr==1190:
                print(n)
                iii=input()
