#!/usr/bin/env python

import webapp2, logging, os
from suds.client import Client
from time import tzset, localtime, strftime

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
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
        self.response.write(str)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

