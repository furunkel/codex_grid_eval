
def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 434839291, 43948294823948932489325274323215, 138193819433072186062142126383219096262136, 138193819433072131683184636804291606934647]
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

from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle.core.utils.timezone import make_aware
from pootle.core.utils.timezone import make_naive
from pootle.core.utils.timezone import make_naive_timezone
from pootle.core.utils.timezone import make_naive_now
from pootle.core.utils.timezone import make_aware_now
from pootle.core.utils.timezone import make_naive_now_with_tz
from pootle.core.utils.timezone import make_aware_now_with_tz_offset
from pootle.core.utils.timezone import make_aware_now_with_tz_offset_utc
from pootle.core.utils.timezone import make_aware_now_with_tz_offset_local
from pootle.core.utils.timezone import make_aware_now_with_tz_offset_utc_local
from pootle.core.utils.timezone