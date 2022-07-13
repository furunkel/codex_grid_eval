
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 2, 2])
    [1, 3, 5, 7]
    """
<|endoftext|># -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_misc.checks import check_names
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path, relative_dir
from pootle_store.util.stats import (
    get_total_words, get_translated_words, get_total_words_word_count,
    get_translated_word_count, get_total_words_word_count_word_count,
    get_translated_word_count_word_frequency, get_total_words_word_frequency_word_count,
    get_translated_word_count_word_frequency_word_count, get_total_words_word_count_word_frequency,
    get_translated_word_count_word_frequency_word_count, get_total_words_word_count_word_frequency_word_count,
    get_translated_word_count_word_frequency_word_count_word_frequency,
    get_total_words_word_count_word_frequency_word_count, get_translated_word_count_word