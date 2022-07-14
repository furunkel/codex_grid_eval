def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "1234?"
    solve("ab") = "BA"
    solve("#a@C") = "c@A#"
    """
    if not s:
        return s
    if s[0] == s[-1]:
        return s
    else:
        return s[1:] + s[0:1] + s[1:]


def main():
    print(solve("1234"))


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
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from pootle.core.delegate import revision
from pootle.core.url_helpers import split_pootle_path
from pootle.core.utils.timezone import datetime_min
from pootle_store.constants import FUZZY, TRANSLATED, UNTRANSLATED
from pootle_store.models import Unit


class UnitManager(models.Manager):

    def get_queryset(self):
        return super(UnitManager, self).get_queryset().filter(
            store__translation_project__project__disabled=False)


@python_2_unicode_compatible
class Unit(models.Model):

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='stores',
        verbose_name=_("Store"),
        related_query_name='stores')
    parent = models.ForeignKey(
        "pootle_store.Unit",
        related_name='children',
        verbose_name=_("Parent"),
        related_query_name='children')
   