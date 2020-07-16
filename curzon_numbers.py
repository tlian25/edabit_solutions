def is_curzon(num):
    numerator = 2 ** num + 1
    denom = 2 * num + 1
    return numerator % denom == 0



def test():
    print(is_curzon(5))
    print(is_curzon(10))

test()