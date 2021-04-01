a, b, c = map(int, input().split())
for i in range(a):
  for j in range(b):
    for k in range(c):
      print('{} {} {}'.format(i,j,k))
print(a*b*c)

#print(f'{i} {j} {k}') -> python 3.6 
