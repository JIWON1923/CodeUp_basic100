num = int(input())
a = list(map(int, input().split()))
student = [0]*23
for i in a: #a는 반복가능한 형태
  student[i-1] += 1
print (" ".join(repr(i) for i in student))
