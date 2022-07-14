def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
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
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_dir
from pootle_store.util import statsd
from pootle_store.util.stats import (
    get_total_changes, get_total_words, get_total_changes_word,
    get_total_changes_word_last_updated, get_total_changes_word_last_created,
    get_total_changes_word_last_updated_verbose)
from pootle_store.util.templatetags import get_templates_for_templates
from pootle_store.util.stats import (
    get_total_changes_word_last_updated_verbose, get_total_changes_word_last_updated,
    get_total_changes_word_last_updated_verbose)
from pootle_store.util.templatetags.store_data import (
    get_template_sources, get_template_sources_for_