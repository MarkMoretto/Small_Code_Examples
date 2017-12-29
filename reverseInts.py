"""
Topic: Reverse Integers
URL: https://leetcode.com/problems/reverse-integer/description/

Author: Mark Moretto
Date Created: 12/29/2017

Challenge:

Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:

    Input: 123
    Output:  321

"""


def revInts(integer, intList=None):
    ints = int(integer)

    if intList == None:
        intList = []
    while ints != 0:
        rem = ints % 10
        intList.append(rem)
        ints = ints // 10
    return intList

def main():
    pass

if __name__ == '__main__':
    main()