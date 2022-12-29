# http://tasks.olimpiada.ru/upload/files/tasks/73/2022/task-info-9;11-gr2-sch-sirius-22-23.pdf

a=int(input())
b=int(input())
t=int(input())
if ((t%a)==0)or((t%b)==0):
    print(0)
else:
    print( min((a-(t%a)),(b-(t%b))))
