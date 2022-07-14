def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lst.count)[0]


def main():
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
from django.utils.functional import cached_property

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import make_aware
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):
    def get_queryset(self):
        return super(UnitManager, self).get_queryset().filter(
            translation__subproject__project__disabled=False
        )


class Unit(models.Model, CachedTreeItem):
    """
    Stores information about a single unit.
    """

    objects = UnitManager()

    class Meta:
        ordering = ["store__pootle_path"]
        unique_together = ("store", "index")
        index_together = ["store", "index"]

    store = models.ForeignKey(
        "pootle_store.Store",
        on_delete=models.CASCADE,
        related_name="stores",
        verbose_name=_("Store"),
        related_query_name="stores",
    )
    index = models.IntegerField(db_index=True)
    state = FUZZY

    class Meta:
        unique_together = ("store", "index")
        index_together = ["store", "index"]

    def __str__(self):
        return "%s (%s)" % (self.index, self.state)

    def get_absolute_