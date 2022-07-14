def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
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
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle.core.utils.timezone import make_naive
from pootle.core.utils.timezone import make_naive_utc
from pootle.core.utils.timezone import make_aware_utc
from pootle.core.utils.timezone import make_naive_local
from pootle.core.utils.timezone import make_aware_local_aware
from pootle.core.utils.timezone import make_aware_local_unaware
from pootle.core.utils.timezone import make_aware_unaware
from pootle.core.utils.timezone import make_aware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware_unaware
from pootle.core.utils.timezone import make_aware_unaware_unaware