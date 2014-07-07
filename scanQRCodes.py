"""
This program is used to take QR codes as input and store them
in the /tmp/krb5cc_1000 which is the default Kerberos ticket
cache.

In the future I will make it more dynamic, allowing you to store
tickets in custom locations, I'll also be adding better checking 
to make sure the whole ticket has been scanned.
"""
import subprocess

#If taken from a file
#code = file("scan.in").read().split("\n")[:-1]

#If taken from the QR code scanner
code = subprocess.check_output(["zbarcam"]).split("\n")[:-1]

#Remove the QR-code: part from each line, separate the time into
#two parts, use the first part as a key, and the second part as
#the value to be stored.
#Will later put in a method of making sure all the tickets are present
for i in range(len(code)): code[i] = code[i][8:]
qrSet = {}
for part in code:
    part = part.split()
    qrSet[int(part[0])] = part[1]

output = ""
for i in range(len(qrSet)):
    output += qrSet[i]

# have to save it to a file so that I can give it to the xxd command
tmp = open("/tmp/tmpqrcode", "w")
tmp.write(output)
tmp.close()

toSave = subprocess.check_output(["xxd", "-p", "-r", "/tmp/tmpqrcode"])
krbTicket = open("/tmp/krb5cc_1000", "w")
krbTicket.write(toSave)
krbTicket.close()
print "Scanned ticket has been added to /tmp/krb5cc_1000"
