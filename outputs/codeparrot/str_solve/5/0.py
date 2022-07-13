
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

def main():
    pass

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
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.file import store_fs_path
from pootle_store.util.stats import (calculate_translation_stats,
                                    get_total_checks,
                                    get_total_words,
                                    get_total_words_word_count)
from pootle_store.util.templatetags import get_templates_for_type
from pootle_store.util.translation import get_translation_percents
from pootle_store.util.util import absolute_real_path_exists
from pootle_store.util.stats import get_total_words_word_count
from pootle_store.util.templatetags.store_tags import get_template_tags
from pootle_store