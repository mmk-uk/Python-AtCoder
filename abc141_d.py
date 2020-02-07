import math
import heapq

n,m = map(int,input().split())

a = list(map(int,input().split()))
a = list(map(lambda x:x*(-1),a))
heapq.heapify(a)

for _ in range(m):
    max = heapq.heappop(a)
    max = max/2
    heapq.heappush(a,max)

a = list(map(lambda x:x*(-1),a))
a = list(map(math.floor,a))

print(sum(a))
