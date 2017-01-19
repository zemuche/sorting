def selection_sort(sequence):
    length = len(sequence)
    for i in range(length-1):
        mini = i
        for j in range(i+1, length):
            if sequence[j] < sequence[mini]:
                mini = j
        sequence[i], sequence[mini] = sequence[mini], sequence[i]
        print(i, mini, sequence)
    return sequence


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    a = original[:]

    print("Original list: {}".format(original))
    print("Selection Sort: {}".format(selection_sort(a)))


if __name__ == "__main__":
    main()
