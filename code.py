import math
import matplotlib.pyplot as plt

top = 1373653
aList = [2, 3]
results = []

for n in range(5,102,2):
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
            c = 1
            for j in range(2 ** r * d):
                c = (c * a) % n
            results[len(results)-1][len(results[len(results)-1])-1].append(c)

for number in results:
    # print(number)
    xTrue = False
    yTrue = False
    for x in number[1]:
        if x == 1 or x == number[0]-1:
            xTrue = True
    for y in number[2]:
        if y == 1 or y == number[0]-1:
            yTrue = True
    if not yTrue or not xTrue:
        print(number[0])

# print(results)


 
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()