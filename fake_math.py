def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second


if __name__ == '__main__':
    result1 = divide(75, 3)
    print(result1)
    result2 = divide(45, 0)
    print(result2)