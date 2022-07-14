def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of the space character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for i in range(len(string)):
        sum = sum + int(string[i])
    return sum % 128

def main():
    """
    Main function
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Check sum for a given string')
    parser.add_argument('-i', '--input', help='The input string to check sum for')
    parser.add_argument('-o', '--output', help='The output string to check sum for')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
    args = parser.parse_args()

    # Check sum
    checksum(args.input)
    checksum(args.output)

    # Print output
    print(args.output)

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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_misc.checks import check_names
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.stats import (
    get_total_words,