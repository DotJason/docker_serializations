import pickle
from checker import run_checker_server

run_checker_server("Pickle", pickle.dumps, pickle.loads, 2001)
