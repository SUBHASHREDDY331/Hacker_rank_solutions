words = []
for _ in range(int(input())):
    words.append(input())
wordsDict = {}
for i in words:
    if i in wordsDict:
        wordsDict[i]+=1
    else:
        wordsDict[i]=1
print(len(wordsDict))
[print(values,end=' ') for values in wordsDict.values()]
    