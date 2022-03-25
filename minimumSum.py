def get_sum(a, b):
    array2int = lambda x: int(''.join(x))
    return array2int(a) + array2int(b)

def get_minimum_sum(K):
    digits = [ digit for digit in str(K) ]
    digits.sort()
       
    a, b = digits[:1], digits[1:]
    sum = get_sum(a, b)

    while True:
        changed = False
        for i, item in enumerate(b):
            a_tmp = a + [item]
            b_tmp = b[:i]+b[i+1:]
            sum_tmp = get_sum(a_tmp, b_tmp)
            if sum_tmp < sum:
                sum = sum_tmp
                best = [a_tmp, b_tmp]
                changed = True
        
        a, b = best
        if not changed or len(a) <= 1 or len(b) <= 1: break

    return sum

tests = [[4891, 67], [8732, 65], [9008, 17],
        [516, 21], [4755, 102]]

for test in tests:
    res = get_minimum_sum(test[0])
    print(test[0], test[1], res, res == test[1])
