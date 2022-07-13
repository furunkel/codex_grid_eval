
def filter_tuples(values: List[Any]) -> List[Tuple]:
    """ Filter given list of any python values only for tuples
    >>> filter_tuples(['a', 3.14, 5])
    []
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
from django.utils.encoding import python_2_unicode_compatible

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import make_aware
from pootle_misc.util import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_to_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (
    get_total_changes, get_total_words, get_total_changes_wordcount,
    get_total_changes_wordcount_wordcount, get_total_changes_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount, get_total_changes_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount, get_total_changes_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount, get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount, get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount, get_total_changes_wordcount_