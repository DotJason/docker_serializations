import json
from checker import run_checker_server

run_checker_server("JSON", json.dumps, json.loads, 2003)
