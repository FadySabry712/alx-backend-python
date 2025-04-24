#!/usr/bin/env python3
""" type annotatd function to retun sum of union of types """
from typing import List


def sum_mixed_list(mxd_lst: List[int | str]) -> float:
    """ return float sum of the mixed values """
    return float(sum(mxd_lst))
