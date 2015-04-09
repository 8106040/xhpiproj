import os

tempfile = open ('/sys/class/thermal/thermal_zone0/temp' )

pitemp = float(tempfile.read()) / 1000

tempupload = file('/home/pi/blobfile/picpu.txt', 'w')

print >> tempupload, pitemp
 
tempupload.close

