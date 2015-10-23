#!/usr/bin/env python

import logging, os
from suds.client import Client
from time import tzset, localtime, strftime

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

os.environ['TZ'] = 'Europe/Moscow'
url = 'http://vigruzki.rkn.gov.ru/services/OperatorRequest/?wsdl'
tzset()

client = Client(url)
result = client.service.getLastDumpDateEx()
hl = "-" * 79 + "\n"
str = hl + "| %-23s | %-23s | %-23s |\n" % ("CurrentTime", "LastDumpDate", "LastDumpDateUrgently")
str = str + hl + "| " + strftime("%Y-%m-%d %H:%M:%S %Z", localtime()) + " | "
str = str + strftime("%Y-%m-%d %H:%M:%S %Z", localtime(result['lastDumpDate']/1000)) + " | "
str = str + strftime("%Y-%m-%d %H:%M:%S %Z", localtime(result['lastDumpDateUrgently']/1000)) + " |\n" + hl
print str
