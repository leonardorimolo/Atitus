
# Trecho 1
for i in range(5):
    pass
print(i)

print('-' * 10)

# Trecho 2
a = 0
for i in range(3):
    print(a)
    a += i
print(a)

print('-' * 10)

# Trecho 3
a = 0
for i in range(2, 10, 2):
    a += i
    print(a)
print(a)

print('-' * 10)

# Trecho 4
a = 10
for i in range(5, 1, -1):
    a -= i
print(a)