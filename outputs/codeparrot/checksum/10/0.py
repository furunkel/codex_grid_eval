def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of lowercase u, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for i in range(len(string)):
        sum = sum + ord(string[i])
    return sum % 128

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum on a file.')
    parser.add_argument('-f', '--file', help='File to check sum on.')
    parser.add_argument('-n', '--number', help='Number of times to check.')
    parser.add_argument('-s', '--size', help='Size of the file to check.')
    parser.add_argument('-r', '--checksum', help='Checksum of the file to check.')
    args = parser.parse_args()

    # Check sum
    checksum(args.file)
    print "Checksum is %s" % checksum(args.file)

    # Check sum on file
    checksum(args.file)
    print "Checksum is %s" % checksum(args.file)

    # Check sum on number
    checksum(args.number)
    print "Checksum is %s" % checksum(args.number)

    # Check sum on size
    checksum(args.size)
    print "Checksum is %s" % checksum(args.size)

    # Check sum on checksum
    checksum(args.checksum)
    print "Checksum is %s" % checksum(args.checksum)

if __name__ == '__main__':
    main()
<|endoftext|># -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest

from django.core.urlresolvers import reverse

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone