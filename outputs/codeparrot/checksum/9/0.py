def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of lowercase u, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for i in range(0, len(string)):
        sum = sum + ord(string[i])
    return sum % 64


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: %s <file> <output>" % sys.argv[0])
        sys.exit(1)

    file = sys.argv[1]
    output = sys.argv[2]

    if not os.path.exists(output):
        print("File %s does not exist" % output)
        sys.exit(1)

    if not os.path.isfile(file):
        print("File %s is not a file" % file)
        sys.exit(1)

    checksum = checksum(open(file, 'rb').read())
    print("Checksum is %s" % checksum)

    if checksum != checksum(open(file, 'rb').read()):
        print("Checksum is not equal to %s" % checksum)
        sys.exit(1)

    print("File %s is OK" % file)


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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import make_aware
from pootle.core.utils.timezone import make_naive
from