def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def main():
    """
    Main function.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate a random string.')
    parser.add_argument('-n', '--name', help='Name of the random string.')
    parser.add_argument('-s', '--seed', help='Seed for the random string.')
    parser.add_argument('-l', '--length', help='Length of the random string.')
    parser.add_argument('-e', '--extra', help='Extra characters to add to the random string.')
    parser.add_argument('-d', '--debug', help='Debug mode.')
    parser.add_argument('-t', '--test', help='Test mode.')
    parser.add_argument('-v', '--verbose', help='Verbose mode.')
    args = parser.parse_args()

    # Set seed
    random.seed(args.seed)

    # Generate random string
    random_string = generate_random_string(args.name, args.length, args.extra, args.debug, args.test, args.verbose)

    # Print results
    print(random_string)

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
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from