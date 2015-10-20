import time, logging, os
from suds.client import Client

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

os.environ['TZ'] = 'Europe/Moscow'
url = 'http://vigruzki.rkn.gov.ru/services/OperatorRequest/?wsdl'
time.tzset()

client = Client(url)
result = client.service.getLastDumpDateEx()

print "lastDumpDate \t\t = \t", time.strftime("%Y-%m-%d %H:%M:%S %Z",
	time.localtime(result['lastDumpDate']/1000))
print "lastDumpDateUrgently \t = \t", time.strftime("%Y-%m-%d %H:%M:%S %Z",
	time.localtime(result['lastDumpDateUrgently']/1000))
