def proc1(x, y):
    p = x * 2.0 + y
    x = x - y
    y = y - x
    print("OOOO: P=",p," X=",x," Y=",y)

def func1(p):
    r = 0
    while (p > 0):
        p = p - 0.6
        r = r + 1
    return r
	
## PROGRAMA PRINCIPAL ##
p = 4.2
q = 1.5
r = 7
s = 4
print("IIII: P=",p," Q=",q," R=",r," S=",s)
proc1(r, s)
print("EEEE: P=",p," Q=",q," R=",r," S=",s)
s = func1(q)
print("UUUU: P=",p," Q=",q," R=",r," S=",s)