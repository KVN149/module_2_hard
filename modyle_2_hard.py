while 1 > 0:
    chec = []
    a = int(input('Введите число от 3 до20: '))
    if a < 3 or a > 20:
        continue
    result = []
    for j in range(1, a):
        for k in range(1, a):
            is_chec = True
            if a % (j + k) == 0 and j != k and j * k not in chec:
                is_chec = False
                result.append(str(j) + str(k))
                chec.append((j) * (k))
                continue
    str = ' '.join([str(elem) for elem in result])
    print(a, '-', format(str).replace(' ', ''))
    del (str)
    continue

