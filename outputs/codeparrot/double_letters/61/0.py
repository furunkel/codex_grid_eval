
def double_letters(string):
    """
    Given a string, return the string, doubling every consonant (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Get the command line arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "input=", "output="])
    except getopt.GetoptError:
        print "Usage: python %s [-h] [-i inputfile] [-o outputfile]" % sys.argv[0]
        sys.exit(2)
    # Process the command line arguments.
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "Usage: python %s [-h] [-i inputfile] [-o outputfile]" % sys.argv[0]
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg
    # Read the input file.
    with open(input_file, "r") as f:
        input_string = f.read()
    # Read the output file.
    with open(output_file, "w") as f:
        f.write(input_string)

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
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle.core.utils.timezone import make_naive
from pootle.core.utils.timezone import make_