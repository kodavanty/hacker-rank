#!/usr/bin/python
import string

# HACKERRANK sorting challenges
def bin_search():
    val = int(raw_input())
    size = int(raw_input())
    string = raw_input()

    array = {}
    i = 0
    for s in string.split():
        array[i] = int(s)
        i = i + 1

    print val
    print size
    for k in array.values():
        print k

if __name__ == "__main__":

    bin_search()
