#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint

import psutil
import platform
from datetime import datetime

#
# def system_info():
#     uname = platform.uname()
#     return {
#         "System": uname.system,
#         "Node Name": uname.node,
#         "Release": uname.release,
#         "Version": uname.version,
#         "Machine": uname.machine,
#         "Processor": uname.processor
#     }
#
#
# def boot_time():
#     boot_time_timestamp = psutil.boot_time()
#     bt = datetime.fromtimestamp(boot_time_timestamp)
#     return {"Boot Time": f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"}
#
#
# if __name__ == '__main__':
#     print("=" * 40, "System Information", "=" * 40)
#     pprint({"System Information": system_info()})
#     print("=" * 40, "Boot Time", "=" * 40)
#     print(boot_time())
#
#     print(psutil.disk_partitions())
