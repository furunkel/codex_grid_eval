
def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains one or more question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "1234"
    solve("1234?") = "?4321"
    solve("ab") = "aB"
    solve("#a@C") = "#a@c"
    """

def main():
    pass

if __name__ == "__main__":
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
from pootle_store.constants import FUZZY, TRANSLATED
from pootle_store.models import Unit
from pootle_store.util import absolute_real_path
from pootle_store.util import TRANSLATED_STATUSES, TRANSLATED_FREQUENCIES
from pootle_store.util import TRANSLATED_FREQUENCIES_MAP
from pootle_store.util import TRANSLATED_LANGUAGES
from pootle_store.util import TRANSLATED_FOLDERS
from pootle_store.util import UNTRANSLATED
from pootle_store.util import TRANSLATED_FOLDERS_MAP
from pootle_store.util import UNTRANSLATED_LANGUAGES_MAP
from pootle_store.util import UNTRANSLATED_FOLDERS_MAP
from pootle_store.util import UNTRANSLATED_LANGUAGES_MAP
from pootle_store.util import UNTRANSLATED_FOLDERS_MAP
from pootle_store.util import UNTRANSLATED_FOLDERS_MAP
from pootle