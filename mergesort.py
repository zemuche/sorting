def merge_sort(alist):
    _merge_sort(alist, 0, len(alist) - 1)
    return alist


def _merge_sort(iterable, first, last):
    mid = (first + last) // 2
    if first < last:
        _merge_sort(iterable, first, mid)
        _merge_sort(iterable, mid+1, last)

        a, z, k = first, mid+1, 0
        temp = [None] * (last - first + 1)
        while a <= mid and z <= last:
            if iterable[a] < iterable[z]:
                temp[k] = iterable[a]
                a += 1
            else:
                temp[k] = iterable[z]
                z += 1
            k += 1

        if a <= mid:
            temp[k:] = iterable[a:mid+1]
        if z <= last:
            temp[k:] = iterable[z:last+1]

        k = 0
        while first <= last:
            iterable[first] = temp[k]
            first += 1
            k += 1


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    my_list = original[:]

    print("Original list: {}".format(original))
    print("Merge Sort: {}".format(merge_sort(my_list)))


if __name__ == "__main__":
    main()
