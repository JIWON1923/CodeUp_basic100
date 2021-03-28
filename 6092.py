num = int(input())
a = list(map(int, input().split()))
d = [0]*23
for i in range(num):
  d[a[i]-1] += 1
print(" ".join(repr(i) for i in d))
