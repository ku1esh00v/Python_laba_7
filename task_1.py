#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print('Неверный размер списка', file=sys.stderr)
        exit(1)

    total = 1
    for item in A:
        if item < 0:
            total *= item

    print(total)