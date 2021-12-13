#a = int(input())
#b = int(input())


def exEuclid(a, b, x, y):
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a

    d = exEuclid(b, a % b, y, x)
    y[0] -= a//b*x[0]
    return d


'''x = [0]
y = [0]
print(str(exEuclid(a, b, x, y))+"="+str(a) +
      "*"+str(x[0])+"+"+str(b)+"*"+str(y[0]))
'''