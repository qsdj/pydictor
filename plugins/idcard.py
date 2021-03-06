#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishprinter, finishcounter, range_compatible, mybuildtime


def idcard_magic(posflag):
    storepath = os.path.join(paths.results_path, "%s_%s_%s%s" %
                             (pystrs.IDCARD_prefix, str(posflag)[-1:], mybuildtime(), pyoptions.filextension))
    posrule = lambda _: str(_) if _ >= 10 else "0" + str(_)
    # month
    value1112 = " ".join(posrule(x) for x in range_compatible(1, 13))
    # day
    value1314 = " ".join(posrule(x) for x in range_compatible(1, 32))
    value1516 = " ".join(posrule(x) for x in range_compatible(1, 100))
    post18 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X")
    value1718 = ""
    if pystrs.default_sex == pystrs.sex_range[0]:
        rand = ("1", "3", "5", "7", "9")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif pystrs.default_sex == pystrs.sex_range[1]:
        rand = ("0", "2", "4", "6", "8")
        for _ in rand:
            for _p in post18:
                value1718 += _ + _p + " "
    elif pystrs.default_sex == pystrs.sex_range[2]:
        rand = " ".join(str(_) for _ in range_compatible(0, 10))
        for _ in rand.split(" "):
            for _p in post18:
                value1718 += _ + _p + " "

    with open(storepath, "a") as f:
        if posflag == pystrs.plug_range[1]:
            for v1112 in value1112.split(" "):
                for v1314 in value1314.split(" "):
                    for v1516 in value1516.split(" "):
                        for v1718 in value1718.split(" "):
                            if v1718 != "":
                                f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head
                                                                                 + v1112 + v1314 + v1516 + v1718 +
                                                                                 pyoptions.tail) + pyoptions.CRLF)
        elif posflag == pystrs.plug_range[0]:
                for v1314 in value1314.split(" "):
                    for v1516 in value1516.split(" "):
                        for v1718 in value1718.split(" "):
                            if v1718 != "":
                                f.write(pyoptions.operator.get(pyoptions.encode)(pyoptions.head
                                                                                 + v1314 + v1516 + v1718 +
                                                                                 pyoptions.tail) + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)
