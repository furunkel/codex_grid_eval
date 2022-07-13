
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every vowel (lower-case or upper-case).
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Get the command line arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print "Error: Invalid options."
        print "Usage: python double_letters.py -i <input> -o <output>"
        sys.exit(2)
    # Process the options.
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "Usage: python double_letters.py -i <input> -o <output>"
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg
    # Run the program.
    double_letters(input)

if __name__ == "__main__":
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
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return super(UnitManager, self).get_queryset().select_related(