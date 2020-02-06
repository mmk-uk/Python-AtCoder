n = int(input())

a = list(map(int,input().split()))

def waru(a,n):
    for i in range(n):
        if a[i]%2==1:
            return False
        else:
            a[i] = a[i]//2
    return True

con = 0
while True:

    if waru(a,n):
        con += 1
    else:
        break

print(con)
