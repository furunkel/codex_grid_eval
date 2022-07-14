def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest last value.
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
from django.utils.encoding import python_2_unicode_compatible

from pootle.core.mixins import CachedTreeItem
from pootle.core.url_helpers import get_editor_filter
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return super(UnitManager, self).get_queryset().filter(
            translation__subproject__project__disabled=False
        )


@python_2_unicode_compatible
class Unit(models.Model):

    project = FuzzyAttribute(
        default=None,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
        db_column="store",
        verbose_name=_("Unit"),
        help_text=_("The unit this unit belongs to"),
    )
    store = FuzzyAttribute(
        default=None,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
        db_column="store",
        verbose_name=_("Store"),
        help_text=_("The store this unit belongs to"),
    )
    state = FuzzyAttribute(
        default=TRANSLATED,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
        db_column="state",
        verbose_name=_("State"),