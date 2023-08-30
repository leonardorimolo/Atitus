n = 123
aux1 = n % 10
aux2 = n // 10
aux3 = aux2 % 10
aux2 = aux2 // 10
n = aux1 * 100
n = n + aux2 * 10
n = n + aux3
print(n)