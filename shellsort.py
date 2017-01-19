def shell_sort(sequence):
    sublist_count = len(sequence)//2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(sequence, start_pos, sublist_count)
        print("After increments of size", sublist_count, "The list is", sequence)
        sublist_count //= 2
    return sequence


def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        key = alist[i]
        j = i
        while j >= gap and alist[j-gap] > key:
            alist[j] = alist[j-gap]
            j -= gap
        alist[j] = key


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    a = original[:]

    print("Original list: {}".format(original))
    print("Shell Sort: {}".format(shell_sort(a)))


if __name__ == "__main__":
    main()
