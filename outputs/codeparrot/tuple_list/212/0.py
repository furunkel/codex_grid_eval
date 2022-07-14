def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lst[-1])[1]


def main():
    """
    Given a list of tuples, write a function that returns the largest value of the tuple with the largest first value.
    """
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9]))


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
        related_query_name='units',
    )
    parent = models.ForeignKey('pootle_store.Store', on_delete=models.CASCADE)
    pootle_path = models.CharField(max_length=255, db_index=True)
    store_revision = models.IntegerField(db_index=True)
    state = FUZZY

    objects = UnitManager()

    class Meta(object):
        unique_together = ('parent