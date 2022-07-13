
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of the newline character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """

def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum on a file.')
    parser.add_argument('-f', '--file', help='File to check sum on.')
    parser.add_argument('-o', '--output', help='Output file name.')
    args = parser.parse_args()

    # Check sum
    sum_file = args.file
    if not os.path.isfile(sum_file):
        print('ERROR: File not found: ' + sum_file)
        sys.exit(1)

    # Read file
    with open(sum_file, 'r') as sum_file_handle:
        sum_data = sum_file_handle.read()

    # Check sum
    checksum_data = checksum(sum_data)
    if checksum_data != checksum(sum_data):
        print('ERROR: Checksum failed: ' + checksum_data)
        sys.exit(1)

    # Print results
    print('Checksum: ' + checksum_data)

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
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware