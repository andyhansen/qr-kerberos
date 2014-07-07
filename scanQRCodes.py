import subprocess

#If taken from a file
#code = file("scan.in").read().split("\n")[:-1]

#If taken from the QR code scanner
code = subprocess.check_output(["zbarcam"])
for i in range(len(code)): code[i] = code[i][8:]

qrSet = {}
for part in code:
    part = part.split()
    qrSet[int(part[0])] = part[1]

output = ""
for i in range(len(qrSet)):
    output += qrSet[i]

print output
