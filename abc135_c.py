n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ms = 0

for i in range(n):
    if a[i]>=b[i]:
        a[i] = a[i]-b[i]
        ms += b[i]
        b[i] = 0
    else:
        b[i] = b[i] - a[i]
        ms += a[i]
        a[i] = 0

    if a[i+1]>=b[i]:
        a[i+1] = a[i+1]-b[i]
        ms += b[i]
        b[i] = 0
    else:
        b[i] = b[i] - a[i+1]
        ms += a[i+1]
        a[i+1] = 0

print(ms)
