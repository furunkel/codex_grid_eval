def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest first value.
    """
    return max(lst, key=lst.count)[0]


def main():
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9]))


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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle_misc.util import ajax_required
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import statsd
from pootle_store.util.stats import (
    get_total_words, get_word_count, get_word_frequency, get_word_count_display,
    get_word_frequency_display, get_word_count_display_plural,
    get_word_count_display_plural, get_word_count_display_plural_plural,
    get_word_count_display_plural_plural, get_word_count_display_plural_plural,
    get_word_count_display_plural_plural, get_word_count_display_plural_plural_plural,
    get_word_count_display_plural_plural_plural, get_word_count_display_plural_plural_plural,
    get_word_count_display_plural_plural_plural, get_word_count_display_plural_plural_plural,
    get_word_count_display_plural_plural_plural, get_word_count_display