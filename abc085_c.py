n,y = map(int,input().split())
yukichi = -1
higuchi = -1
noguchi = -1
for i in range(n+1):
    for j in range(n+1-i):
        if 10000*i+5000*j+1000*(n-i-j)==y:
            yukichi = i
            higuchi = j
            noguchi = n-i-j

print("{} {} {}".format(yukichi,higuchi,noguchi))
