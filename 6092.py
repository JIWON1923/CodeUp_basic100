num = int(input())
a = list(map(int, input().split()))
student = [0]*23
for i in a:
  student[i-1] = a.count(i) # count 함수 사용
print (' '.join(repr(i) for i in student))
