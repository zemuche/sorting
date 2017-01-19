def bubble_sort(sequence):
    passes = len(sequence) - 1
    exchange = True
    while passes > 0 and exchange:
        exchange = False
        for i in range(passes):
            if sequence[i] > sequence[i+1]:
                exchange = True
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
        passes -= 1
        print(len(sequence)-passes, sequence)
    return sequence, len(sequence) - passes


def main():
    original = [5, 1, 20, 13, 9, 37, 28, 6, 4, 2, 3, 7, 25]
    a = original[:]

    print("Original list: {}".format(original))
    print("Bubble Sort: {}".format(bubble_sort(a)))


if __name__ == "__main__":
    main()
