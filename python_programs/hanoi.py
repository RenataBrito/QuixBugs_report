
def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(hanoi(height - 1, start, helper))
        steps.append((start, end))
        steps.extend(hanoi(height - 1, helper, end))

    return steps

#if __name__ == "__main__":
    #print(hanoi(2,3,1))
    #[[0, 1, 3], []]
#    pass