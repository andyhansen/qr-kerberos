import sys
import qrcode

fileName = "creds.out"
if len(sys.argv) > 1:
    fileName = sys.argv[1]

text = file(fileName).read().replace("\n", "")
limit = 796
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
