#!/usr/bin/env python3
"""
Author : richardsmacbook <richardsmacbook@localhost>
Date   : 2026-01-05
Purpose: Howler
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename'
                        )

    args = parser.parse_args()

    if os.path.isfile(args.positional):
        with open(args.positional, 'r') as fh:
            args.positional = fh.read().rstrip('\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.outfile:
        with open(args.outfile, 'w') as out_fh:
            out_fh.write(f'{args.positional.upper()}\n')
    else:
        print(f'{args.positional.upper()}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
