
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Store
from pootle_store.util import absolute_real_path
from pootle_store.util import relative_real_path
from pootle_store.util import relative_real_path_to_dir
from pootle_store.util import relative_real_path_to_dir_path
from pootle_store.util import relative_real_path_to_dir_path
from pootle_store.util import relative_real_path_to_dir_path_join
from pootle_store.util import relative_real_path_to_dir_path_join
from pootle_store.util import relative_real_path_to_dir_path_join_path
from pootle_store.util import relative_real_path_to_dir_path_join_path
from pootle_store.util import relative_real_path_to_dir_path_join_path_join_path
from pootle_store.util import relative_real_path_to_dir_path_join_path_join_path
from pootle_store.util import relative_real_path_to_dir_path_join_path_join_path
from pootle_store.util import relative_