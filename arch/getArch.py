import platform
import sys


def get_arch():
    return platform.architecture()[0]
