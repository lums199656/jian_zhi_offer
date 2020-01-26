def replaceSpace(s):
    list_ = list(s)
    for (index, item) in enumerate(list_):
        if item == " ":
            list_[index] = '%20'
    return "".join(list_)


if __name__ == '__main__':
    print(replaceSpace('We Are Happy'))
