#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import prod

if __name__ == 'main':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print('Неверный размер списка', file=sys.stderr)
        exit(1)

    total = prod(item for item in A if item < 0)
    print(total)
