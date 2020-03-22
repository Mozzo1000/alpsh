import platform
import distutils.spawn
import itertools

byte_standard = [
    (1024 ** 5, ' PB'),
    (1024 ** 4, ' TB'),
    (1024 ** 3, ' GB'),
    (1024 ** 2, ' MB'),
    (1024 ** 1, ' KB'),
    (1024 ** 0, (' byte', ' bytes')),
    ]

byte_verbose = [
    (1024 ** 5, (' petabyte', ' petabytes')),
    (1024 ** 4, (' terabyte', ' terabytes')),
    (1024 ** 3, (' gigabyte', ' gigabytes')),
    (1024 ** 2, (' megabyte', ' megabytes')),
    (1024 ** 1, (' kilobyte', ' kilobytes')),
    (1024 ** 0, (' byte', ' bytes')),
    ]


def convert_byte_size(bytes, format=byte_standard):
    for factor,suffix in format:
        if bytes >= factor:
            break
    amount = int(bytes/factor)
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix


def get_os():
    return platform.system()


def get_alpsh_installation():
    return distutils.spawn.find_executable('alpsh')


def split_list(l, condition):
    groupby = itertools.groupby(l, condition)
    return [list(group) for k, group in groupby if not k]


def split_pipes(cmd):
    result = split_list(cmd, (lambda x: x == '|'))
    return result
