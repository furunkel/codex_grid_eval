def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 256, add the integer value of uppercase X, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for i in range(256):
        sum = sum + int(string[i])
    return sum % 256


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: %s <file> <output>" % sys.argv[0])
        sys.exit(1)

    file = sys.argv[1]
    output = sys.argv[2]

    if not os.path.isfile(file):
        print("File not found: %s" % file)
        sys.exit(1)

    with open(file, "r") as f:
        data = f.read()

    checksum = checksum(data)
    print("Checksum: %s" % checksum)

    if checksum != data:
        print("Checksum failed: %s" % checksum)
        sys.exit(1)

    print("Checksum OK")


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
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return super(UnitManager, self).