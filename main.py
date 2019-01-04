#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Molecules Assessment
"""
__author__ = "tgentry300, mdshepard"

import itertools


def rectangle_tuples(x):
    # num_range = range(1, int(x + 1))
    # pairs = list(itertools.combinations_with_replacement(num_range, 2))
    # pairs.reverse()
    # print pairs

    pairs = [(w, h) for w in range(2, 11) for h in range(w, 11)]
    # Sort from largest rectangle area to smallest rectangle area
    pairs.sort(key=lambda x : x[0] * x[1], reverse=True)
    print pairs


def check_strings(list_of_strings):
    # print list_of_strings[:2]
    pass


# def function to loop through strings and rectangle sizes

def best_fit(w, h, across1, across2, down1, down2):
    """Tries to fit a rectangle into a set of 4 molecule strings returns true if found a fit"""
    # across and down check for intersection
    for a1 in range(1, 12 - w):
        for d1 in range(1, 12 - h):
            if accross1[a1] != down1[d1]:
                continue
            # If it comes past this continue, might have a rectangle that works
            for a2 in range(1, 12 - w):
                if accross2[a2] != down1[d1 + h]:
                    continue
                    # TODO finish this


def main():
    strings_list = ['O I M D I H E I A F N L', 'C H J D B J M H P J K D',
                    'L C B J O J G I E K B O', 'K A I N L H L O L B E J']

    check_strings(strings_list)
    rectangle_tuples(8)


if __name__ == '__main__':
    """Runs main function"""
    main()
