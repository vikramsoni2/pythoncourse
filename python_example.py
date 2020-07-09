def z(a, b, c):
    d = 0.0
    e = 0.0

    for i in range(a, b):
        if i % c == 0:
            d = d + 1
        else:
            e = e + 1
    if d > e:
        return d
    else:
        return e
        
x = z(1, 100, 3)