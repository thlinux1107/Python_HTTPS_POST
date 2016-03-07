import sys, httplib
import datetime

HOST = "APIDemo.IPCharge.net:443"
API_URL = "/IPCHAPI/RH.aspx"
now = datetime.datetime.now()

 
def do_request(xml_location):
        """HTTP XML Post request, by thlinux"""
        StartTime = now
        request = open(xml_location,"r").read()
        webservice = httplib.HTTPS(HOST)
        webservice.putrequest("POST", API_URL)
        webservice.putheader("Host", HOST)
        webservice.putheader("User-Agent","Python post")
        webservice.putheader("Content-type", "text/xml")
        webservice.putheader("Content-length", "%d" % len(request))
        webservice.endheaders()
        webservice.send(request)
        statuscode, statusmessage, header = webservice.getreply()
        result = webservice.getfile().read()
        EndTime = now

        print request
        print statuscode, statusmessage, header
        print result

        f = open("result_log.txt","a") #opens file with name of "result_log.txt"
        f.write(">>>>>>>>>>>>>>>>> Transaction Started %s \n" % str(StartTime)[:19])
        f.write("%s \n" % str(request))
        f.write("%s \n" % str(result))
        f.write(">>>>>>>>>>>>>>>>> Transaction Ended %s \n" % str(EndTime)[:19])
        f.close()
 
do_request("myfile.xml")
