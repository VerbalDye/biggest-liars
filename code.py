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
    results.append({})
    for a in aList:
        for r in range(1, m + 1):
            c = a
            for j in range(2^r * (d-1)):
                c = (c * a) % n
            results[len(results)]