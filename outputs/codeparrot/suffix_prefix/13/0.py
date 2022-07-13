
def all_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
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

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import make_aware
from pootle_misc.util import ajax_required
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import SIDEBAR
from pootle_store.util import TRANSLATED_NAMES
from pootle_store.util import TRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED
from pootle_store.util import TRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from pootle_store.util import UNTRANSLATED_NAMES_MAP
from po