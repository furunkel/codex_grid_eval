def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[1]


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
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.stats import get_translation_states
from pootle_store.util.templatetags import get_templates_for_unit
from pootle_store.util.stats import get_translation_source_stats
from pootle_store.util.templatetags.store_stats import (
    get_store_stats, get_store_stats_for_unit)
from pootle_store.util.stats import get_source_translation_stats
from pootle_store.util.templatetags.store_stats import get_store_stats_for_source
from pootle_store.util.templatetags.store_stats import get_store_stats_for_store
from pootle_store.util.templatetags.store_stats import get_store_stats_for_store_unit
from pootle_store.util.templatetags.store_stats import get_store_stats_for_store_unit
from pootle_store.util.templatetags.store_stats import get_store_stats_for_source