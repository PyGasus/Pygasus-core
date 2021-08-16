#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint

import psutil
import platform
from datetime import datetime


def system_info():
    uname = platform.uname()
    return {
        "System": uname.system,
        "Node Name": uname.node,
        "Release": uname.release,
        "Version": uname.version,
        "Machine": uname.machine,
        "Processor": uname.processor
    }


if __name__ == '__main__':
    print("=" * 40, "System Information", "=" * 40)
    pprint({"System Information": system_info()})
