
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('prefix')
    ['prefix', 'prefi', 'pref', 'pre', 'pr', 'p']
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

from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path
from pootle_store.util import relative_real_path
from pootle_store.util import statsd
from pootle_store.util import statsd_key
from pootle_store.util import statsd_total_changes
from pootle_store.util import get_translation_states
from pootle_store.util import get_translation_source_stats
from pootle_store.util import get_translation_source_wordcount
from pootle_store.util import get_translation_source_wordcount_display
from pootle_store.util import get_translation_source_wordcount_display_key
from pootle_store.util import get_translation_source_wordcount_display_key_plural
from pootle_store.util import get_translation_source_wordcount_display_key_plural
from pootle_store.util import get_translation_source_wordcount_display_key_plural_plural
from pootle_store.util import get_translation_source_wordcount_display_key_plural_plural
from pootle_store.util import get_translation_source_wordcount_display_key_plural_plural
from pootle_store.