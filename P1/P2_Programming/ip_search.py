
def IP_searching(binaryStrIP, binaryRecordList):
    longestPrefix = -1
    res = -1
    for binaryRecord in binaryRecordList:
        lenth = len(binaryRecord[0])
        tempStr = binaryStrIP[0 : lenth]
        if tempStr == binaryRecord[0]:
            if binaryRecord[2] > longestPrefix:
                longestPrefix = binaryRecord[2]
                res = binaryRecord[1]
    if res == -1:
        return False
    return res


list1 = [["192.168.0.0", 16, 10000],
        ["192.168.0.0", 24, 50000]]
binaryRecordList = [['1100000010101000', 0, 16],
                    ['110000001010100000000000',1, 24]]

bStr = "11000000101010000000000000000001" #192.168.0.1

temp = IP_searching(bStr, binaryRecordList)
print(temp)
print(list1[temp])