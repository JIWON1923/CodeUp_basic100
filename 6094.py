num = int(input())
a = list(map(int, input().split()))
result = a[0]
for i in a:
  if result > i:
    result = i
print(result)
