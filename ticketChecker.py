import subprocess
import sys
import binascii

def hexFileToBinaryFile(infile, outfile):
    """
    Opens infile and assumes it is a hex file stored in ascii.
    Will convert the file to binary form then store the converted
    fields in the outfile location.
    """
    hexTicket = file(infile).read().replace("\n", "")
    binTicket = binascii.unhexlify(hexTicket)
    savedTicket = open(outfile, "w")
    savedTicket.write(binTicket)
    savedTicket.close()

def has_kerberos_ticket(location="/tmp/tmpticket"):
    """
    Checks in the given location to see if it is a valid ticket cache. Will
    return true if it is, or false if it is not
    """
    return True if subprocess.call(['klist', location, '-s']) == 0 else False

def has_code(code):
    """
    Basic extra checker, this will later be modified to check for more advanced
    things such as GPS coords, or a more advanced code. In its current state this 
    method can be thought as a placeholder.
    """
    if code == "thisisthecode":
        return True
    else:
        return False

print has_kerberos_ticket(location="/tmp/krb5cc_1000")
