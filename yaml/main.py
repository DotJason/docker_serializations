from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper
from checker import run_checker_server


def dump_wrapper(data):
    return dump(data, Dumper=Dumper)


def load_wrapper(data):
    return load(data, Loader=Loader)


run_checker_server("YAML", dump_wrapper, load_wrapper, 2006)
