#! /bin/bash

#import packages
import pexpect
import time

#spawn a shell prompt
child = pexpect.spawn('/bin/bash')
#send the curl command to download file from noaa file will be called gearlandingsdata.txt
child.sendline("curl 'http://www.st.nmfs.noaa.gov/pls/webpls/MF_GEAR_LANDINGS.RESULTS' -H 'Host: www.st.nmfs.noaa.gov' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://www.st.nmfs.noaa.gov/commercial-fisheries/commercial-landings/landings-by-gear/index' -H 'Cookie: __utma=194499183.103505879.1423701115.1425005836.1425066719.8; __utmz=194499183.1424309347.3.2.utmcsr=yahoo|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=194499183.3.10.1425066719; __utmt=1; __utmc=194499183' -H 'Connection: keep-alive' --data 'qspecies=ALL+SPECIES+INDIVIDUALLY&qreturn=Species+Locator&qyearfrom=1950&qyearto=2013&qstate=California&qgear_type=%25&qoutput_type=DOWNLOAD+ASCII+FILE+-+UNIX' > gearlandingsdata.txt")

#wait for download to finish
time.sleep(30)



#print completion line
print 'The Data has been downloaded'
#get only the lines after the 6th line and saves it as data_w_o_header.txt
child.sendline("tail -n+6 gearlandingsdata.txt > data_w_o_header.txt")
#wait 10 seconds
time.sleep(10)

print "The Header has been removed"
