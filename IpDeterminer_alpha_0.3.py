import datetime
import msvcrt 
from datetime import timedelta
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
def finalReturn(inp):
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
    return decRes
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
def ipDeterminer(ipAdd):
    datetime_object = datetime.datetime.now()
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
    binBroadcast = binCount(binNetAdd, allPieces(binHosts))
    binLastHost = binCount(binBroadcast, "-1")
    binNextNet = binCount(binBroadcast, "1")
    print("Original IP address        ", finalStringConvert(binIpPiece))
    print("Subnet Mask:               ", finalStringConvert(binSubnetPiece))
    print("Net Address:               ", finalStringConvert(binNetAdd))
    print("First Host:                ", finalStringConvert(binFirstHost))
    print("Last Host:                 ", finalStringConvert(binLastHost))
    print("Broadcast:                 ", finalStringConvert(binBroadcast))
    print("Hosts:                     ", hostCounter(binHosts))
    print("NextNet:                   ", finalStringConvert(binNextNet))
    datetime_object2 = datetime.datetime.now()
    print("\nCalculation took", str(float(((datetime_object2 - datetime_object).microseconds)*0.001)) + "ms\nHave a nice day")
    return finalReturn(binNextNet)
while(True):
    answer = int(input("Simple Subnet(1) or VLSM(2)"))
    if answer == 1:
        ipAdd = str(input("Enter ip address:\n"))
        ipDeterminer(ipAdd)
    elif answer == 2:
        startIp = input("enter start IP")
        lst = []
        dct = {}
        reverseDct = {}
        subnet = ""
        while(True):
            inpTxt = input("what is the name of the department(enter \"exit\" to exit)")
            if inpTxt == "exit":
                break
            else:
                inpNum = int(input("enter how many do they need(enter \"exit\" to exit)"))
                if inpNum == "exit":
                    break
            lst.append(inpNum)
            reverseDct[inpNum] = inpTxt
        lst.sort()
        lst.reverse()
        for i in lst:
            dct[reverseDct[i]] = i
        for i in dct:
            nm = dct[i]
            if nm > 32766:
                subnet = "/16"
            elif nm > 16382:
                subnet = "/17"
            elif nm > 8190:
                subnet = "/18"
            elif nm > 4094:
                subnet = "/19"
            elif nm > 2046:
                subnet = "/20"
            elif nm > 1022:
                subnet = "/21"
            elif nm > 510:
                subnet = "/22"
            elif nm > 254:
                subnet = "/23"
            elif nm > 126:
                subnet = "/24"
            elif nm > 62:
                subnet = "/25"
            elif nm > 30:
                subnet = "/26"
            elif nm > 14:
                subnet = "/27"
            elif nm > 6:
                subnet = "/28"
            elif nm > 2:
                subnet = "/29"
            else:
                subnet = "/30"
            ipAdd = ""
            ipAdd = "{0}{1}".format(startIp, subnet)
            print("-------------------------", i, "-------------------------")
            startIp = ipDeterminer(ipAdd)
    else:
        print("error")
        
