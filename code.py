import math

top = 1373653
aList = [2, 3]
results = []

for n in range(5,101,2):
    m = 0
    d = n - 1
    i = True
    while i == True:
        if d % 2 == 0:
            d = d/2
            m += 1
        else:
            d = math.floor(d)
            i = False
    results.append([n])
    for a in aList:
        results[len(results)-1].append([])
        for r in range(m):
            c = a
            for j in range(2^r * (d-1)):
                c = (c * a) % n
            results[len(results)-1][len(results[len(results)-1])-1].append(c)

print(results)