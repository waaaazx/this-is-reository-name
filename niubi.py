def LOOP(a, b, MAX):
    # a is the smaller.
    if b < a:
        a, b = b, a

    x = L = y = B = 1
    Min = 8888.8
    SN = [1]

    def c_sign(NUM):
        if NUM > 0:
            s0 = 0
        else:
            s0 = 1
        return s0

    while x < MAX+1 and y < int(MAX * a / b):
        s = a * x - b * y
        SN.append(c_sign(s))
        if Min > abs(s):
            Min = abs(s)
            L = x
            B = y

        x += 1
        if SN[-1] != SN[-2]:
            y += 1

        # print(f"Difference = {s}\nx = {x}, y = {y}")
    return L, B, Min
