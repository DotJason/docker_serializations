from msgpack import dumps, loads
from checker import run_checker_server

run_checker_server("MessagePack", dumps, loads, 2007)
