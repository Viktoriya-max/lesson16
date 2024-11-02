from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


if __name__ == '__main__':
    result1 = divide(67, 39)
    print(result1)
    result2 = divide(56, 0)
    print(result2)
