a, r, n = map(int, input().split())
i, result = 1, a
while ( i < n ):
  result *= r
  i += 1
print(result)
