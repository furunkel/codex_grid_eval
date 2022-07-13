
def filter_lists(values: List[Any]) -> List[List[Any]]:
    """ Filter given list of any python values only for lists
    >>> filter_lists([1, 2, 3, 3.6, 'abc', {}, [], (1,)])
    [[]]
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
from pootle_store.util import absolute_real_path_in_pootle_store
from pootle_store.util import relative_real_path_in_pootle_store
from pootle_store.util import relative_real_path_in_template_store
from pootle_store.util import relative_real_path_in_template_store
from pootle_store.util import relative_real_path_in_store
from pootle_store.util import relative_real_path_in_user_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store.util import relative_real_path_in_tp_store
from pootle_store