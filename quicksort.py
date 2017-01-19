import statistics as stat


def quick_sort(iterable):
    less = []
    equal = []
    greater = []

    if len(iterable) > 1:
        three = [iterable[0], iterable[len(iterable)//2], iterable[-1]]
        pivot = stat.median(three)
        for i in iterable:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    
    else:
        return iterable


def main():
    original = [5, 1, 6, 4, 2, 3, 7, 20, 13, 9, 37, 28, 25]
    a = original[:]

    print("Original list: {}".format(original))
    print("Quick Sort: {}".format(quick_sort(a)))


if __name__ == "__main__":
    main()
