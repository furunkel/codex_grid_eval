def f(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    return max(lst, key=lst.count)[1]


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
from pootle_misc.checks import check_names
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path, relative_real_path
from pootle_store.util import relative_to_real_path, relative_to_dir
from pootle_store.util import UNTRANSLATED
from pootle_store.util import TRANSLATED
from pootle_store.util import UNTRANSLATED_SUFFIX
from pootle_store.util import UNTRANSLATED_PATH
from pootle_store.util import UNTRANSLATED_PATH_PREFIX
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX_LENGTH
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX_LENGTH_CHECK
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX_LENGTH_CHECK
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX_LENGTH_CHECK
from pootle_store.util import UNTRANSLATED_PATH_SUFFIX_