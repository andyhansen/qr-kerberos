import binascii

"""
This opens up the creds.out file, removes new line characters, converts the contents
to binary format then stores the binary as a file in the /tmp/ directory. The idea is
that this takes decoded kerberos tickets from the QR codes, puts them in the right format
then stores them in the tmp directory where they can actually be used.

This could be made as a function which takes a file with hex contents and saves it 
converted to binary in the given destination.
"""

hexTicket = file("creds.out").read().replace("\n", "")
binTicket = binascii.unhexlify(hexTicket)
savedTicket = open("/tmp/binticket", "w")
savedTicket.write(binTicket)
savedTicket.close()
