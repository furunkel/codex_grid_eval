def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
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

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return super(UnitManager, self).get_queryset().select_related(
            "store", "store__parent", "store__translation_project"
        )


class Unit(models.Model):
    """
    Stores information about a single unit of a store.
    """

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="stores",
        verbose_name=_("Store"),
        related_query_name="stores",
    )
    parent = models.ForeignKey(
        "pootle_store.models.Directory",
        on_delete=models.CASCADE,
        related_name="child_units",
        verbose_name=_("Parent"),
        related_query_name="parent",
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the unit."),
    )
    state = FUZZY

    # Unit fields
    source_f = models.ForeignKey(
        "pootle_store.Unit",
        on_delete=