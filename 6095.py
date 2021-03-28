num = int(input())
game = [[0]*19 for i in range(19)]
for i in range(num):
  a, b = map(int, input().split())
  game[a-1][b-1] = 1
for i in game:
  print(" ".join(repr(j) for j in i))
