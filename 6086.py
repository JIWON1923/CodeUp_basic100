a = int(input())
result = 0
for i in range(a+1):
  if result >= a:
    break
  result += i

print(a if a < 3 else result)
