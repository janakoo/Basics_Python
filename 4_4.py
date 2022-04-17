def factor(n):
    s= 1
    for i in range(1,n+1):
        s = s*i
        yield s

n=10
for i in factor(n):
    print(i)