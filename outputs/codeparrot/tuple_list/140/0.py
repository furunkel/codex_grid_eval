def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest last value.
    """
    return max(lst, key=lst.count)


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
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (
    get_total_words, get_translated_words, get_total_words_fuzzy,
    get_translated_percentages, get_total_words_fuzzy_nofuzzy,
    get_total_words_nofuzzy, get_translated_percentages_nofuzzy,
    get_translated_words_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_translated_percentages_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_translated_words_nofuzzy_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_translated_percentages_nofuzzy_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_translated_words_nofuzzy_nofuzzy, get_total_words_nofuzzy_