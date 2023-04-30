from xml_marshaller import xml_marshaller
from checker import run_checker_server

run_checker_server("XML", xml_marshaller.dumps, xml_marshaller.loads, 2002)
