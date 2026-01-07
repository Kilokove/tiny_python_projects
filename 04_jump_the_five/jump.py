#!/usr/bin/env python3
"""
Author : richardsmacbook <richardsmacbook@localhost>
Date   : 2026-01-05
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    ENCODING_TABLE = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
                      '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    args = get_args()
    str_arg = args.text

    for char in str_arg:
        print(ENCODING_TABLE.get(char, char), end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
