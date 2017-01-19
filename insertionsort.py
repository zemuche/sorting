def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        key = sequence[i]
        j = i
        while j > 0 and sequence[j-1] > key:
            sequence[j] = sequence[j-1]
            j -= 1
        sequence[j] = key
    return sequence


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    a = original[:]

    print("Original list: {}".format(original))
    print("Insertion Sort: {}".format(insertion_sort(a)))


if __name__ == "__main__":
    main()
