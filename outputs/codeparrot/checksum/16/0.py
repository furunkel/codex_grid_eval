def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of a question mark, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for char in string:
        sum = sum + int(char)
    return sum % 128

def main():
    """
    Main function
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum on a file')
    parser.add_argument('-f', '--file', help='File to check sum on')
    parser.add_argument('-n', '--number', help='Number of times to check')
    parser.add_argument('-s', '--size', help='Size of the file to check')
    parser.add_argument('-c', '--checksum', help='Checksum of the file to check')
    args = parser.parse_args()

    # Check sum
    checksum = checksum(args.file)
    if checksum != args.checksum:
        print("Checksum mismatch: %s != %s" % (args.checksum, checksum))
        sys.exit(1)

    # Check sum on file
    sum = checksum(args.file)
    if sum != args.checksum:
        print("Checksum mismatch: %s != %s" % (args.checksum, checksum))
        sys.exit(1)

    # Print results
    print("Checksum: %s" % checksum)
    print("Checksum: %s" % sum)

if __name__ == '__main__':
    main()
<|endoftext|># -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import logging

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.mixins import CachedTreeItem
from pootle.core