
def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists(['a', 3.14, 5])
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
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util.stats import (calculate_translated_words,
                                      get_total_words,
                                      get_translated_words)
from pootle_store.util.templatetags import get_templates_for_templates
from pootle_store.util.templatetags.store_tags import (get_templates_for_pootle_path,
                                                         get_templates_for_store)
from pootle_store.util.stats import get_total_words_of_unit
from pootle_store.util.translation import get_translation_project
from pootle_store.util.stats import get_total_words_of_unit_changes
from pootle_store.util.translation import get_translation_project
from pootle_store.util.stats import get_total_words_of_unit_changes_for_store
from pootle_store.util.translation import get_translation_project_dir
from pootle_store.util.stats import get_total_words_of_unit_changes_for_unit
from pootle_store.util.stats import get_total_words_of_unit_changes_for_store