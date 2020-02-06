#入力
n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int,input().split())))


t = 0
gx = 0
gy = 0
x = 0
y = 0
can = True
for i in range(n):
    gt = p[i][0]
    gx = p[i][1]
    gy = p[i][2]
    flag = False
    while True:
        if gx>x:
            x+=1
            t+=1
        elif gx<x:
            x-=1
            t+=1
        else:
            if gy>y:
                y+=1
                t+=1
            elif gy<y:
                y-=1
                t+=1
            else:
                if t>gt:
                    break
                elif t==gt:
                    flag = True
                    break
                else:
                    x+=1
                    t+=1
    if flag==False:
        can = False
        break

if can:
    print("Yes")
else:
    print("No")
