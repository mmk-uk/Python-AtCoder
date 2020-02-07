n = int(input())

p = list(reversed(list(range(1,n+1))))

r = set(range(1,n+1))

m = []

for i in range(n):
    f = True
    a = 1
    b = 1
    while f:
        while (a*p[i]-b)<=n and f:
            if a*p[i]-b in r:
                r.remove(a*p[i]-b)
                m.append((a*p[i]-b)%p[i])
                f = False
                break
            a += 1
        b += 1

print(sum(m))

#n = int(input())

#print((n*(n-1)//2))
