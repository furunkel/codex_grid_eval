def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for char in string:
        sum = sum * ord(char)
    return sum % 64


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum.')
    parser.add_argument('-c', '--checksum', help='Check sum with checksum', required=True)
    parser.add_argument('-d', '--directory', help='Check sum in directory', required=True)
    parser.add_argument('-f', '--file', help='Check sum in file', required=True)
    parser.add_argument('-o', '--output', help='Check sum in output file', required=True)
    args = parser.parse_args()

    # Check sum
    checksum(args.checksum)

    # Check sum with checksum
    checksum(args.checksum)

    # Check sum with directory
    checksum(args.directory)

    # Check sum in file
    checksum(args.file)

    # Check sum in output file
    checksum(args.output)

if __name__ == '__main__':
    main()
<|endoftext|># -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_