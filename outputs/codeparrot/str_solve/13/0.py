
def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "1234?"
    solve("ab") = "Ba"
    solve("#a@C") = "c@a#"
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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.stats import (
    get_total_words, get_translated_words, get_total_words_word_count,
    get_translated_word_count, get_total_words_word_count_word_frequency,
    get_translated_word_count_word_frequency, get_total_words_word_count_word_frequency_weekly,
    get_total_words_word_frequency_weekly_total, get_total_words_word_frequency_weekly_total_words,
    get_translated_word_count_word_frequency_weekly_total_words, get_translated_word_count_word_frequency_weekly_total_words,
    get_translated_word_count_word_frequency_weekly_total_words_weekly,
    get_total_words