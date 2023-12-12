#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    lst = list(map(float, input().split()))

    # Find the number of the minimum list item
    min_index = lst.index(min(lst))

    # Find the sum of the list items located between the first and second negative elements
    neg_indexes = [i for i, x in enumerate(lst) if x < 0]

    if len(neg_indexes) >= 2:
        sum_between = sum(lst[neg_indexes[0] + 1:neg_indexes[1]])
        print(f"The number of the minimum element: {min_index}")
        print(f"The sum of the elements between the first and second negative: {sum_between}")
    else:
        print("There are no two negative elements in the list!", file=sys.stderr)
