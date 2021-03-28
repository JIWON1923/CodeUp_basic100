num = int(input())
a = list(map(int, input().split()))
print(" ".join(repr(i) for i in reversed(a)))
