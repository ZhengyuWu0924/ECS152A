def IP_searching(binaryStrIP, binaryRecordList):
    longestPrefix = -1
    res = -1
    for binaryRecord in binaryRecordList:
        lenth = len(binaryRecord[0])
        tempStr = binaryStrIP[0:lenth]
        if tempStr == binaryRecord[0]:
            if binaryRecord[2] > longestPrefix:
                longestPrefix = binaryRecord[2]
                res = binaryRecord[1]
    if res == -1:
        return False
    return res


data_base = open("./DB_091803.txt", "r")
list1 = []
list2 = []
index = 0
for data in data_base:
    if(data == "\n"):
        continue
    error_flag = 0
    ip_data = data.split()[0]
    prefix_len = int(data.split()[1])
    as_number = int(data.split()[2])
    temp = ""
    for i in range(0, 4):
        if (ip_data.split('.')[i] == ""):
            error_flag = 1
        else:
            temp += bin(int(ip_data.split('.')[i]))[2:].rjust(8, '0')
    if (error_flag):
        temp = ""
        continue
    prefix = temp[:int(prefix_len)]
    list2.append([prefix, index, prefix_len])
    list1.append([ip_data, prefix_len, as_number])
    index += 1

data_base.close()
IPlist = open("./IPlist.txt", "r")
output_file = open("./output.txt", "w")
for user_input in IPlist:
    input_error_flag = 0
    bin_user_input = ""
    for j in range(0, 4):
        if (user_input.split('.')[j] == ""):
            input_error_flag = 1
        else:
            bin_user_input += bin(int(user_input.split('.')[j]))[2:].rjust(
                8, '0')
    output = IP_searching(bin_user_input, list2)
    output_file.write(list1[output][0] + "/" + str(list1[output][1]) + " " +
                      str(list1[output][2]) + " " + user_input)

IPlist.close()
output_file.close()
