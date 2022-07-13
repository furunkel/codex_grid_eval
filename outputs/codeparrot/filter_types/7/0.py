
def filter_dictionarys(values: List[Any]) -> List[Dict[Any, Any]]:
    """ Filter given list of any python values only for dictionarys
    >>> filter_dictionarys([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [{}]
    """
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

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import make_aware
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (
    get_total_words, get_translated_words, get_total_words_fuzzy,
    get_translated_words_fuzzy, get_total_words_fuzzy_nofuzzy,
    get_total_words_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_total_words_nofuzzy_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_total_words_fuzzy_fuzzy, get_total_words_fuzzy_nofuzzy,
    get_total_words_nofuzzy_fuzzy, get_total_words_nofuzzy_nofuzzy,
    get_total_words_nofuzzy_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_total_words_nofuzzy_nofuzzy_nofuzzy, get_total_words_nofuzzy_nofuzzy,
    get_total_words_nofuzzy_nofuzzy_nofuzzy, get_total