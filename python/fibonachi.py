def fib(n):
    List = [0,1]
    for i in range(2,n+1):
        List.append(List[i-1] + List[i-2])
    return List[n]
n = 10
print(fib(n))