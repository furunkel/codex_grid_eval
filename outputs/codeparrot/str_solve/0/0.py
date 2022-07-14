def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "?4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if not s:
        return s
    if s[0] == s[-1] == '"':
        return s[1:-1]
    else:
        return s


def main():
    """The main function"""
    s = solve("1234")
    print(s)


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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path
from pootle_store.util import TRANSLATED_STATUSES, TRANSLATED_FOLLOWERS
from pootle_store.util import TRANSLATED_FOLLOWERS_NAMES
from pootle_store.util import get_translation_project
from pootle_store.util import TRANSLATED_LANGUAGES
from pootle_store.util import get_translation_project_dir
from pootle_store.util import get_translation_project_dir_path
from pootle_store.util import get_translation_project_translation_project_dir
from pootle_store.util import get_translation