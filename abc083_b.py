n,a,b = map(int,input().split())

sum = 0

for i in range(1,n+1):
    s = 0
    for j in range(len(str(i))):
        s += int(str(i)[j])
    if s >=a and b >= s:
        sum += i

print(sum)
