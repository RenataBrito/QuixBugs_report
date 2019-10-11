
def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend([i] * count)

    return sorted_arr

"""
def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(arr):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr
"""

if __name__ == "__main__":
    vet1 = []
    vet2 = [3, 11, 2, 9, 1, 5]
    vet3 = [50,20,45,10,69]
    print (bucketsort(vet1,1))
    print (bucketsort(vet2,12))
    print (bucketsort(vet3,70))
pass
