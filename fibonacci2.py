def generate_fabonacci(n):
    lst=[]
    a=0
    b=1
    for i in range (0,n):
        lst.append(a)
        a, b = b, a+b
    return lst