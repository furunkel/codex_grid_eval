def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest third value.
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
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.file import store_file_class
from pootle_store.util.stats import (
    get_total_changes, get_total_words, get_total_changes_wordcount,
    get_total_changes_wordcount_wordcount, get_total_changes_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount, get_total_changes_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount,
    get_total_changes_wordcount_wordcount_wordcount_wordcount