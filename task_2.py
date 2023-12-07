#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    lst = list(map(float, input().split()))

    # Find the number of the minimum list item
    min_index = sorted(range(len(lst)), key=lambda i: lst[i])[0]

    # Find the sum of the list items located between the first and second negative elements
    neg_indexes = sorted([i for i in range(len(lst)) if lst[i] < 0])

    if len(neg_indexes) >= 2:
        sum_between = sum(lst[neg_indexes[0] + 1:neg_indexes[1]])
        print(f"The number of the minimum element: {min_index}")
        print(f"The sum of the elements between the first and second negative: {sum_between}")
    else:
        print("There are no two negative elements in the list!", file=sys.stderr)