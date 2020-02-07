n = int(input())
b = list(map(int,input().split()))

a = []
a.append(b[0])

for i in range(n-1):
    if i==n-2:
        a.append(b[i])
    else:
        if b[i]<b[i+1]:
            a.append(b[i])
        else:
            a.append(b[i+1])

print(sum(a))
