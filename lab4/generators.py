def squares(n):
    for i in range(n+1):
        yield i**2

def evens(n):
    for i in range(n):
        if i%2==0:
            yield i

def divisible_3_4(n):
    for i in range(n):
        if i%3==0 and  i%4==0:
            yield i

def squares(a,b):
    for i in range(a,b):
        yield i**2

def downto(n):
    for i in range(n,-1,-1):
        yield i

for num in _function_name_here_():       # type: ignore
    print(num, end=' ')
