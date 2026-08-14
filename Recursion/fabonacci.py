# fibonacci series : 0,1,1,2,3,5,8,_ _ _ _ _ _

def fabonacci(n):
    if n ==0 or n ==1:
        return n
    return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(2))