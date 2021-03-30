import datetime
import msvcrt 
from datetime import timedelta
ipAdd = "192.168.1.2/24"
#ipAdd = str(input("Enter ip address:\n"))
datetime_object = datetime.datetime.now()
def binarPieceConvert(tmp):
    myTmp = []
    for i in range(0, 32, 8):
        myTmp.append(tmp[i:i+8])
    return myTmp
def decToBinarPieces(inp):
    res = []
    for i in range(4):
        res.append(str('0'*(8-len(bin(int(inp[i]))[2:])) + bin(int(inp[i]))[2:]))
    return res
def binToDecimalPieces(inp):
    res = []
    for i in range(4):
        res.append(int(inp[i], base=(2)))
    return res
def finalStringConvert(inp):
    decRes = ""
    binRes = ""
    myNum = 0
    for i in binToDecimalPieces(inp):
        decRes += str(i)
        binRes += inp[myNum]
        myNum += 1
        if myNum != 4:
            decRes += "."
            binRes += " "
    return decRes + "   (" + binRes + ")"
def binCompare(binLeft, binRight):
    res = []
    for i in range(4):
        tmp = ""
        for j in range(8):
            if binLeft[i][j] == '1' and binRight[i][j] == '1':
                tmp += '1'
            else:
                tmp += '0'
        res.append(tmp)
    return res
def binCount(binList, binNum):
    return binarPieceConvert(bin(int(allPieces(binList), base=(2)) + int(binNum, base=(2)))[2:])
def allPieces(binList):
    listNum = ''
    for i in binList:
        listNum += i
    return listNum
def hostCounter(inp):
    res = ""
    for i in inp:
        res += i
    res = str(int(res, base=(2)) - int("1", base=(2)))
    return res
if ipAdd.count(".") == 3 and ipAdd.count("/") == 1:
    ipPiece = ipAdd.split(".")
    ipPiece += ipPiece[3].split("/")
    ipPiece.remove(ipPiece[3])
    for i in range(4):
        if int(ipPiece[i]) > 255 or int(ipPiece[i]) < 0:
            raise Exception("IP out of range")
    if int(ipPiece[4]) > 30 or int(ipPiece[4]) < 8:
        raise Exception("Subnetmask out of range")
else:
    raise Exception("not a propper IP adress")
binIpPiece = decToBinarPieces(ipPiece)
tmp = "1"*int(ipPiece[4]) + "0"*(32-int(ipPiece[4]))
binSubnetPiece = binarPieceConvert(tmp)
binNetAdd = binCompare(binIpPiece, binSubnetPiece)
binHosts = []
for i in binSubnetPiece:
    tmp = ''
    for j in i:
        if j == '0':
            tmp += '1'
        else:
            tmp += '0'
    binHosts.append(tmp)
binFirstHost = binCount(binNetAdd, "1")
binLastHost = binCount(binNetAdd, allPieces(binHosts))
binBroadcast = binCount(binLastHost, "1")
binNextNet = binCount(binBroadcast, "1")
print('\n\nOriginal IP address', finalStringConvert(binIpPiece))
print("\nSubnet Mask:", finalStringConvert(binSubnetPiece))
print("\nNet Address:", finalStringConvert(binNetAdd))
print("\nFirst Host:", finalStringConvert(binFirstHost))
print("\nLast Host:", finalStringConvert(binLastHost))
print("\nBroadcast:", finalStringConvert(binBroadcast))
print("\nHosts:", hostCounter(binHosts))
print("\nNextNet:", finalStringConvert(binNextNet))
datetime_object2 = datetime.datetime.now()
print("\nCalculation took", str(float(((datetime_object2 - datetime_object).microseconds)*0.001)) + "ms\nHave a nice day")
s = msvcrt.getch()