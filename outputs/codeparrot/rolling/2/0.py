
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([434839248, 43, 43948294823948932489324839483924, 138193819389123891238193193893893821938921, -54378957489578927489327489])
    [434839248, 43, 43, 43, -54378957489578927489327489]
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

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return Unit.objects.filter(store=self.model)

    def get_by_path(self, path):
        return self.get(pootle_path=path)


@python_2_unicode_compatible
class Unit(models.Model, CachedTreeItem):

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='stores',
        verbose_name=_('Store'),
        related_query_name='stores',
    )
    parent = models.ForeignKey('pootle_store.Unit', related_name='children',
                               verbose_name=_('Parent'), null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    parent_path = models.CharField(max_length