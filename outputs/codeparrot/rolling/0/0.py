
def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 1, 1, 1]
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
from pootle.core.utils.timezone import make_aware
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return Unit.objects.filter(store=self.model)

    def get_by_path(self, path):
        return self.get(pootle_path=path)


@python_2_unicode_compatible
class Unit(models.Model):

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
    parent_path = models.CharField(max_length=255, verbose_name=_('Parent Path'))
    pootle_path = models.CharField(max_length=255, verbose_name=_('Path'))
    state = FUZZY

    objects = UnitManager()

    class Meta:
        ordering = ['store__pootle