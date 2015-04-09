#!/bin/bash 

raspistill -o /home/pi/blobfile/pic.jpg

sudo python /home/pi/xhpiproj/pi_cpu_temp.py

sudo python /home/pi/xhpiproj/env_temp.py

sudo python /home/pi/xhpiproj/azure_blob_upload.py