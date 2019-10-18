
def flatten(arr):
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                yield y

        else:
            yield x
            


if __name__ == "__main__":
    a = [[[1, [], [2, 3]], [[4]], 5]]
    print(flatten(a))
    #[[[[1, [], [2, 3]], [[4]], 5]], [1, 2, 3, 4, 5]]
