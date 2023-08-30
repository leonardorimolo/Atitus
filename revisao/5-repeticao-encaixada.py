d = -4
l = 0
j = 3
for i in range(2, 5):
    while j >= 0:
        k = i + j
        j -= 1
        d += 1
        if d > 0:
            j -= d
        print(f"J = {j}, K = {k} L = {l}")
    j = 0
    l += i
print(f"I = {i}")