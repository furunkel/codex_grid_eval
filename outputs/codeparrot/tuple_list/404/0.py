def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lst.count)


def main():
    print(f(range(10)))


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
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_misc.util import datetime_to_timestamp
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_to_real_path, relative_to_dir
from pootle_store.util import UNTRANSLATED, UNTRANSLATED_DIR
from pootle_store.util import UNTRANSLATED_FS_PREFIX
from pootle_store.util import UNTRANSLATED_FS_SUFFIX
from pootle_store.util import UNTRANSLATED_FS_PREFIXES
from pootle_store.util import UNTRANSLATED_FS_SUFFIXES
from pootle_store.util import UNTRANSLATED_FS_PREFIXES_MAP
from pootle_store.util import UNTRANSLATED_FS_SUFFIX_MAP
from pootle_store.util import UNTRANSLATED_FS_SUFFIX_MAP
from pootle_store.util import UNTRANSLATED_FS_PREFIXES_MAP
from pootle_store.util import UNTRANSLATED_FS_SUFFIX_