import datetime
from datetime import timedelta
ipAdd = "192.168.1.2/24"
#ipAdd = str(input("Enter ip address: "))
datetime_object = datetime.datetime.now()
decNetAdd = ""
dotOccurs = []
slashOcccurs = 0
slashSubnet = 0
binSubnet = ""
binIp = ""
decSubnet = ""
binNetAdd = ""
tmp = ""
binHosts = ""
decHosts = 0
binFirstHost = ""
decFirstHost = ""
binLastHost = ""
decLastHost = ""
binBroadcast = ""
decBroadcast = ""
binNextNet = ""
decNextNet = ""

#tmp2 = ipadd.split(".")
#tmp2[3] = tmp2[3].split("/")
#           FUNCTIONS             ########################

def findAll(where, what):
    where = str(where)
    what = str(what)
    occurs = []
    while where.count(what) != 0:
        num = where.find(".")
        where = where[num + 1:]
        if len(occurs) != 0:
            num += occurs[-1] + 1 
        occurs.append(num)
#    print(occurs)
    return occurs


#         OTHER CODE            ############################

dotOccurs = findAll(ipAdd, ".")
slashOcccurs = ipAdd.find("/")
if len(dotOccurs) != 3:
    print("error")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      missing fourth octet       !!!!!!!!!!!!!!!!!!!!!!!!!!
######################### first octet ######################################################## second octet ############################################################## third octet ##########################
if int(ipAdd[0:dotOccurs[0]]) > 0 & int(ipAdd[0:dotOccurs[0]]) < 255 & int(ipAdd[dotOccurs[0]+1:dotOccurs[1]]) > 0 & int(ipAdd[dotOccurs[0]+1:dotOccurs[1]]) < 255 & int(ipAdd[dotOccurs[1]+1:dotOccurs[2]]) > 0 & int(ipAdd[dotOccurs[1]+1:dotOccurs[2]]) < 255:
#    print("ok")
    print()
else:
    raise Exception("IP out of range")
if "/" in ipAdd:
#    print("has a subnet")
    slashSubnet = int(ipAdd[slashOcccurs + 1:])
    for i in range(slashSubnet):
        binSubnet += '1'
    for i in range(32 - slashSubnet):
        binSubnet += '0'
    for i in range(0, 32, 8):
        decSubnet += str(int(binSubnet[i:i+8], base=2))
        if i != 24:
            decSubnet += "."
else:
    print("error")

################# binIp


tmp = bin(int(ipAdd[0:dotOccurs[0]]))[2:]
if len(tmp) < 8:
    zeros = 8-len(tmp)
    tmp = "{0}{1}".format("0"*zeros, tmp)
binIp += tmp

tmp = bin(int(ipAdd[dotOccurs[0]+1:dotOccurs[1]]))[2:]
if len(tmp) < 8:
    zeros = 8-len(tmp)
    tmp = "{0}{1}".format("0"*zeros, tmp)
binIp += tmp

tmp = bin(int(ipAdd[dotOccurs[1]+1:dotOccurs[2]]))[2:]
if len(tmp) < 8:
    zeros = 8-len(tmp)
    tmp = "{0}{1}".format("0"*zeros, tmp)
binIp += tmp

tmp = bin(int(ipAdd[dotOccurs[2]+1:slashOcccurs]))[2:]
if len(tmp) < 8:
    zeros = 8-len(tmp)
    tmp = "{0}{1}".format("0"*zeros, tmp)
binIp += tmp


for i in range(32):
    if int(binIp[i]) == 1 & int(binSubnet[i]) == 1:
        binNetAdd += '1'
    else:
        binNetAdd += '0'

for i in range(0, 32, 8):
        decNetAdd += str(int(binNetAdd[i:i+8], base=2))
        if i != 24:
            decNetAdd += "."

for i in binSubnet:
    if i == '0':
        binHosts += '1'
    else:
        binHosts += '0'

decHosts = int(binHosts, base=2) - 1

binFirstHost = bin(int(binNetAdd, base=2) + 1)[2:]

for i in range(0, 32, 8):
        decFirstHost += str(int(binFirstHost[i:i+8], base=2))
        if i != 24:
            decFirstHost += "."



tmp = 0
binLastHost = bin(int(binNetAdd, base=2) + int(binHosts, base=2) - int('1', base=2))[2:]
for i in range(0, 32, 8):
        decLastHost += str(int(binLastHost[i:i+8], base=2))
        if i != 24:
            decLastHost += "."

binBroadcast = bin(int(binNetAdd, base=2) + int(binHosts, base=2))[2:] # binlasthost + 1
for i in range(0, 32, 8):
        decBroadcast += str(int(binBroadcast[i:i+8], base=2))
        if i != 24:
            decBroadcast += "."

binNextNet = bin(int(binBroadcast, base=2) + int('1', base=2))[2:]
for i in range(0, 32, 8):
        decNextNet += str(int(binNextNet[i:i+8], base=2))
        if i != 24:
            decNextNet += "."

print("\n")
print("IPv4 address:",ipAdd, "(" + binIp + ")", "in binary")
print("\n")
print("IPv4 subnet mask:",decSubnet, "(" + binSubnet + ")", "in binary")
print("IPv4 net address:",decNetAdd, "(" + binNetAdd + ")", "in binary")
print("First host:", decFirstHost, "(" + binFirstHost + ")", "in binary")
print("Last host:", decLastHost, "(" + binLastHost + ")", "in binary")
print("Broadcast:", decBroadcast, "(" + binBroadcast + ")", "in binary")
print("Number of Hosts:", decHosts)
print("NextNet:", decNextNet, "(" + binNextNet + ")", "in binary")
datetime_object2 = datetime.datetime.now()
print("\nCalculation took", str(float(((datetime_object2 - datetime_object).microseconds)*0.001)) + "ms\nHave a nice day")
a = input()