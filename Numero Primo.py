def conta(n):
    for num in range(n+1):
        if num == 0:
            continue
        if n%num == 0:
            resul.append('1')
        else:
            continue
    
n = 1
while True:
    resul = []
    n += 1
    conta(n)
    if len(resul) == 2:
        print(n)
