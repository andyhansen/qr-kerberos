"""
Takes the tickets out of the default Kerberos ticket cache and
stores them in QR codes. Not much flexability yet, but it will be
added as needed.

"""

import sys
import qrcode
import subprocess

# Note that the 1000 here is the userid of the current user
if subprocess.call(["ls", "/tmp/krb5cc_1000"]) == 2:
    exit("No kerberos ticket convert")

text = subprocess.check_output(["xxd", "-p", "/tmp/krb5cc_1000"]).replace("\n", "")
#fileName = "creds.out"
#if len(sys.argv) > 1:
#    fileName = sys.argv[1]

#text = file(fileName).read().replace("\n", "")

#no real reason I picked this limit
limit = 1800
current = 0
total = round(len(text) / (limit*1.0))
qrArray = []
while current < total:
    qrArray.append(str(current) + " " + text[current*limit : (current+1)*limit])
    current+=1


for i, code in enumerate(qrArray):
    img = qrcode.make(code)
    output = open("ticket-" + str(i) + ".png", "w")
    img.save(output, "PNG")
    output.close()

subprocess.call(["kdestroy"])
