


def get_minimum_sum(K):
    digits = [ int(digit) for digit in str(K) ]
    digits.sort()
    n_digits = len(digits)

    min_sum = int('9'*n_digits)
    best = None
    


    for i, a in enumerate(digits):
        remain_digits_0 = digits[:i]+digits[i+1:] 
        for j, b in enumerate(remain_digits_0):
            remain_digits_1 = remain_digits_0[:j]+remain_digits_0[j+1:]
            for l, c in enumerate(remain_digits_1):
                remain_digits_2 = remain_digits_1[:l]+remain_digits_1[l+1:]
                for m, d in enumerate(remain_digits_2):
                    int()
                    


    return 0

tests = [[4891, 67], [8732, 65], [9008, 17],
        [516, 21], [4755, 102]]

for test in tests:
    res = get_minimum_sum(test[0])
    print(test[0], test[1], res, res == test[1])
    break