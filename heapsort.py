def heap_sort(iterable):
    # Convert list to heap
    length = len(iterable) - 1
    least_parent = int(length / 2)
    for i in range(least_parent, -1, -1):
        move_down(iterable, i, length)

    # Flatten heap into sorted array
    for i in range(length, 0, -1):
        if iterable[0] > iterable[i]:
            swap(iterable, 0, i)
            move_down(iterable, 0, i-1)

    return iterable


def move_down(iterable, first, last):
    largest = (2 * first) + 1
    while largest <= last:
        # Right child exists and is larger than left child
        if (largest < last) and (iterable[largest] < iterable[largest+1]):
            largest += 1

        # Right child is larger than parent
        if iterable[largest] > iterable[first]:
            swap(iterable, largest, first)
            # Move down to largest child
            first = largest
            largest = (2 * first) + 1
        else:
            return      # Force exit


def swap(a, x, y):
    a[x], a[y] = a[y], a[x]


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    my_list = original[:]

    print("Original list: {}".format(original))
    print("Heap Sort: {}".format(heap_sort(my_list)))


if __name__ == "__main__":
    main()
