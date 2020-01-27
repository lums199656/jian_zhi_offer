import datetime


def Find_1(target, array):
    # 运行时间：449ms
    # 占用内存：5724k
    i = 0
    j = len(array[0]) - 1
    while i < len(array) and j >= 0:
        if target > array[i][j]:
            i += 1
        elif target < array[i][j]:
            j -= 1
        else:
            return True
    return False


def Find_2(target, array):
    # 运行时间：339ms
    # 占用内存：5660k
    # array_ = flatten(array)
    array_ = [i for item in array for i in item]
    # if target in array_:
    #     return True
    # return False
    for i in array_:
        if target == i:
            return True
    return False


def Find_3(target, array):
    # 运行时间：305ms
    # 占用内存：5652k
    for i in array:
        if target in i:
            return True
    return False


if __name__ == '__main__':
    target = 15
    array_ = [[1, 2, 8, 9],
              [2, 4, 9, 12],
              [4, 7, 10, 13],
              [6, 8, 11, 15]]
