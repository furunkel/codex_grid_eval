def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains more than one question mark, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    if not s:
        return s
    if len(s) == 1:
        return s
    if s[0] == s[-1]:
        return s
    else:
        return s[1:] + s[:1]


def main():
    """The main function"""
    print(solve("ab"))


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
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (calculate_changes, get_changes_dict,
                                     get_last_changes)
from pootle_store.util.templatetags.store_tags import get_tags_by_path
from pootle_store.util.stats import get_total_changes
from pootle_store.util.templatetags.store_tags import get_tags_by_path_stats
from pootle