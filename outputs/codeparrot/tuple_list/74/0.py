def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
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
        return Unit.objects.filter(store=self.model)

    def get_units(self):
        return self.get_queryset().order_by('store__pootle_path')

    def get_units_with_access(self, user):
        return self.get_queryset().filter(store__pootle_path__startswith=user.username)

    def get_units_with_access_in_db(self, user):
        return self.get_queryset().filter(store__pootle_path__startswith=user.username)

    def get_units_with_access_in_db_and_parent(self, user):
        return self.get_queryset().filter(store__pootle_path__startswith=user.username)

    def get_units_with_access_in_parent_and_translation_project(self, user):
        return self.get_queryset().filter(store__pootle_path__startswith=user.username)

    def get_units_with_