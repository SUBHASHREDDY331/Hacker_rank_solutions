from datetime import datetime
for _ in range(int(input())):

    t1=input()
    t2=input()
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    print(int(abs((t1-t2).total_seconds())))