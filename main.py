import platform
import psutil

from arch.getArch import get_arch
from sysInfo.getSysInfo import get_system_info
from cpuInfo.getCPUInfo import get_cpu_info, get_cpu_percentage

if __name__ == '__main__':
    print(get_arch())
    print("--"*10)
    print(get_system_info())

    print(get_cpu_info())
    print(get_cpu_percentage())
