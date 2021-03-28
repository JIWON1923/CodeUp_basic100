h, w = map(int, input().split())
game = [[0]*w for i in range(h)]
n = int(input())
for i in range(n):
  l, d, x, y = map(int, input().split())
  for i in range(0,l):
    if d == 0:
      game[x-1][y+i-1] = 1
    else:
      game[x+i-1][y-1] = 1
for i in game:
  print(" ".join(repr(j)for j in i))
