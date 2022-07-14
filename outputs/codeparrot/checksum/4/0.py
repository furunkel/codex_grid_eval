def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 128, add the integer value of the newline character, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """
    sum = 0
    for char in string:
        sum = sum + ord(char) - 128
    return sum % 128

def main():
    """
    Main function.
    """
    if len(sys.argv) != 3:
        print "Usage: %s <file> <output>" % sys.argv[0]
        sys.exit(1)
    file = sys.argv[1]
    output = sys.argv[2]
    if not os.path.isfile(file):
        print "File %s does not exist" % file
        sys.exit(1)
    if not os.path.isfile(output):
        print "Output file %s does not exist" % output
        sys.exit(1)
    checksum(open(file, 'rb').read())

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
from pootle.core.plugin import getter
from pootle.core.url_helpers import split_pootle_path
from pootle_app.models.permissions import check_user_permission
from pootle_language.models import Language
from pootle_project.models import Project
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Store
from pootle_store.util import absolute_real_path


@pytest.mark.django_db
def test_get_path_with_no_parent(client):
    """Tests that the path is returned without a parent."""
    path = "/foo/bar"
   