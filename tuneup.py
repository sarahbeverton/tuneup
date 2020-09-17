#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Sarah Beverton"

import cProfile
import pstats
import timeit
from collections import Counter


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    movies_dict = Counter(movies)
    duplicates = [k for k, v in movies_dict.items() if v > 1]
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
    result = t.repeat(repeat=7, number=3)
    averages = [num/3 for num in result]
    print("Best time across 7 repeats of 3 runs per repeat:", min(averages))


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
