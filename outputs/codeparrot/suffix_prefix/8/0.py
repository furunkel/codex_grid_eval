
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('reverse the result!!!')
    ['reverse the result!!!', 'reverse the result!!', 'reverse the result!', 'reverse the result', 'reverse the resul', 'reverse the resu', 'reverse the res', 'reverse the re', 'reverse the r', 'reverse the ', 'reverse the', 'reverse th', 'reverse t', 'reverse ', 'reverse', 'revers', 'rever', 'reve', 'rev', 're', 'r']
    """
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
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (get_total_words, get_translated_words,
                                   get_total_words_word_count)
from pootle_store.util.templatetags.store_tags import get_all_tags
from pootle_store.util.stats import get_word_count
from pootle_store.util.templatetags.store_tags import get_word_count_word_counts
from pootle_store.util.templatetags.store_tags import get_word_count_word_frequency
from pootle_store.util.templatetags.store_tags import get_word_count_word_frequency_count
from