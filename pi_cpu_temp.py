import os

tempfile = open ('/sys/class/thermal/thermal_zone0/temp' )

pitemp = float(tempfile.read()) / 1000

tempupload = file('/home/pi/blobfile/tempfile.txt', 'w')

print >> tempupload, pitemp
 
tempupload.close

