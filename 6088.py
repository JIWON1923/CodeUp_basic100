a, d, n = map(int, input().split())
i, result = 1, a
while ( i< n ):
  result += d
  i += 1
print(result)
