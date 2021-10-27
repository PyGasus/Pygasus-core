import psutil


def get_cpu_info():
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()
    return {"cpu_max_frequency": cpu_freq.max,
            "cpu_count": cpu_count}


def get_cpu_percentage():
    return psutil.cpu_percent()
