k,m =input().split()
sqrt_a=[]
for i in range(int(k)):
    l = list(map(int, input().split()))
    n=l[0]
    l.remove(l[0])
    
    max_l=max(l)
    sqrt_a.append(max_l**2)
print(sum(sqrt_a)%int(m))
